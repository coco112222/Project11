from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size=(400,600)
Window.clearcolor=(0,1,1,1)
b='''
<Design>:
    GridLayout:
        cols:1
        rows:2
        size:root.width,root.height
        
        TextInput:
            id:tex
            multiline:False
            text:"0"
            size_hint:(1,0.2)
            font_size:50
        GridLayout:
            rows:4
            cols:4
            spacing:5
            padding:6
            Button:
                text:"1"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"2"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"3"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"4"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"5"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"6"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"7"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"8"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"9"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"0"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"+"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"-"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"*"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"/"
                on_press:
                    root.input()
                    tex.text+=self.text
            Button:
                text:"="
                on_press:root.pressed()
            Button:
                text:"CE"
                on_press:
                    root.clear()'''
Builder.load_string(b)

class Design(Widget):
    
    def input(self):
        
        if self.ids.tex.text=="0":
            self.ids.tex.text=""
        elif self.ids.tex.text=="Error":
            self.ids.tex.text=""
        else:
            pass
    def clear(self):
        self.ids.tex.text="0"

    def pressed(self):
        try:
            self.ids.tex.text=str(eval(self.ids.tex.text))
        except Exception as e:
            self.ids.tex.text="Error"


class CalculatorHero(App):
    def build(self):
        return Design()
    
ap=CalculatorHero()
ap.run()