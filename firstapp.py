import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
kivy.require("1.9.0")
class myRoot(BoxLayout):
    def __init__(self):
        super(myRoot,self).__init__()
    def genrate_num(self):
        self.random_label.text=str(random.randint(10,100))

class randomNum(App):
    def build(self):
        return myRoot()

randomNum1=randomNum()
randomNum1.run()