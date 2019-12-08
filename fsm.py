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
        send_text_message(event, "歡迎使用YCBot\n今天你想看什麼電影呢；)\n每天為你挑選適合你的影片\n輸入「地區」或「類型」\n用你最喜歡的方式搜尋！")

    def on_enter_type(self, event):
        send_text_message(event, "輸入\n「愛情」、「科幻」、「劇情」、「動畫」\n尋找你想看的電影類型")
    def on_enter_region(self, event):
        send_text_message(event, "可輸入\n「美洲」、「歐洲」、「台灣」、「亞洲」\n尋找你想看的區域的電影")

    def on_enter_love(self, event):
        send_text_message(event, " 2018《誰先愛上他的》\n「當有個人跟你說，他想當個正常人然後離開你，從那之後的每一天，就是一萬年」")
        self.go_back(event)
    def on_enter_animate(self, event):
        send_text_message(event, "2017《COCO》\n「The real death is that no one in the world remembers you.」")
        self.go_back(event)
    def on_enter_scifi(self, event):
        send_text_message(event, " 2014 《彗星來的那一夜》\n「科技來自於人性，那麼科幻就來自遺憾」")
        self.go_back(event)
    def on_enter_drama(self, event):
        send_text_message(event, "2016《最美的安排》\n「Just be sure to notice the collateral beauty. It's the profound connection to everthing.」")
        self.go_back(event)
    def on_enter_am(self, event):
        send_text_message(event, "2018《猛毒》\n「有時候別人會阻止我們，但到最後改變世界的是我們」")
        self.go_back(event)
    def on_enter_eu(self, event):
        send_text_message(event, "2015《丹麥女孩》\n「You helped bring Lili to life but she's always been there.  」")
        self.go_back(event)
    def on_enter_tai(self, event):
        send_text_message(event, "2017《血觀音》\n「 世界上最可怕的不是眼前的刑罰，而是無愛的未來」")
        self.go_back(event)
    def on_enter_as(self, event):
        send_text_message(event, "2017《與神同行》\n「不要為過去的事，浪費新的眼淚」")
        self.go_back(event)