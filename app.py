import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["start", "welcome", "type", "region","love","animate","scifi","drama","am","eu","tai","as"],
    transitions=[
        {
            "trigger": "advance",
            "source": "start",
            "dest": "welcome"
        },
        {
            "trigger": "advance",
            "source": "welcome",
            "dest": "type",
            "conditions": "is_going_to_type",
        },
        {
            "trigger": "advance",
            "source": "welcome",
            "dest": "region",
            "conditions": "is_going_to_region",
        },
        {
            "trigger": "advance",
            "source": "type",
            "dest": "love",
            "conditions": "is_going_to_love",
        },
        {
            "trigger": "advance",
            "source": "type",
            "dest": "animate",
            "conditions": "is_going_to_animate",
        },
        {
            "trigger": "advance",
            "source": "type",
            "dest": "scifi",
            "conditions": "is_going_to_scifi",
        },
        {
            "trigger": "advance",
            "source": "type",
            "dest": "drama",
            "conditions": "is_going_to_drama",
        },
        {
            "trigger": "advance",
            "source": "region",
            "dest": "am",
            "conditions": "is_going_to_am",
        },
        {
            "trigger": "advance",
            "source": "region",
            "dest": "eu",
            "conditions": "is_going_to_eu",
        },
        {
            "trigger": "advance",
            "source": "region",
            "dest": "tai",
            "conditions": "is_going_to_tai",
        },
        {
            "trigger": "advance",
            "source": "region",
            "dest": "as",
            "conditions": "is_going_to_as",
        },
        {"trigger": "go_back", "source": ["love","animate","scifi","drama","am","eu","tai","as"], "dest": "welcome"},
    ],
    initial="start",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)


parser = WebhookParser(channel_secret)

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
