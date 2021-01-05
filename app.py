import kivy
kivy.require("1.0.6") # replace with your current kivy version !

from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.label import Label

class ButtonCustom(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "CLICK ME"

    def on_press(self, *args, **kwargs):
        print(args, kwargs)
        self.text = "NEW"


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.b1 = ButtonCustom()
        self.b1.on_press = self.b1_clicked

        self.label = Label(text="MIRKO")

    def b1_clicked(self):
        self.label.text = "MARKO"

    def build(self):
        return self.b1


if __name__ == '__main__':
    MyApp().run()
