from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_type(self, event):
        text = event.message.text
        return text == "類型"
    def is_going_to_region(self, event):
        text = event.message.text
        return text == "地區"

    def is_going_to_love(self, event):
        text = event.message.text
        return text == "愛情"    
    def is_going_to_animate(self, event):
        text = event.message.text
        return text == "動畫"  
    def is_going_to_scifi(self, event):
        text = event.message.text
        return text == "科幻"  
    def is_going_to_drama(self, event):
        text = event.message.text
        return text == "劇情"  
    def is_going_to_am(self, event):
        text = event.message.text
        return text == "美洲"  
    def is_going_to_eu(self, event):
        text = event.message.text
        return text == "歐洲"  
    def is_going_to_tai(self, event):
        text = event.message.text
        return text == "台灣"  
    def is_going_to_as(self, event):
        text = event.message.text
        return text == "亞洲"
    
    def on_enter_welcome(self, event):
        send_text_message(event, "歡迎使用")

    def on_enter_type(self, event):
        send_text_message(event, "可輸入\n「愛情」、「科幻」、「劇情」、「動畫」")
    def on_enter_region(self, event):
        send_text_message(event, "可輸入\n「美洲」、「歐洲」、「台灣」、「亞洲」")

    def on_enter_love(self, event):
        send_text_message(event, "《誰先愛上他的》")
        self.go_back(event)
    def on_enter_animate(self, event):
        send_text_message(event, "《COCO》")
        self.go_back(event)
    def on_enter_scifi(self, event):
        send_text_message(event, "《彗星來的那一夜》")
        self.go_back(event)
    def on_enter_drama(self, event):
        send_text_message(event, "《最美的禮物》")
        self.go_back(event)
    def on_enter_am(self, event):
        send_text_message(event, "《猛毒》")
        self.go_back(event)
    def on_enter_eu(self, event):
        send_text_message(event, "《放牛班的春天》")
        self.go_back(event)
    def on_enter_tai(self, event):
        send_text_message(event, "《血觀音》")
        self.go_back(event)
    def on_enter_as(self, event):
        send_text_message(event, "《與神同行》")
        self.go_back(event)