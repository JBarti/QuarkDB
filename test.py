from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

from QuarkAPI.Controllers import FilterNew, StoreTypes
from QuarkAPI import Quark

api = Quark()

class FilterCheckbox(CheckBox):
    def __init__(self, filter_type, filter_val, **kwargs):
        super().__init__(**kwargs)
        self.filter_type = filter_type
        self.filter_val = filter_val


class CheckBoxScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.input_lbl = Label(text="search")
        self.search_input = TextInput(multiline=False)
        self.checkboxes = [
            (Label(text="Steam"), FilterCheckbox("store", StoreTypes.steam)),
            (Label(text="G2A"), FilterCheckbox("store", StoreTypes.g2a)),
        ]

        self.add_widget(self.input_lbl)
        self.add_widget(self.search_input)
        for lbl, check in self.checkboxes:
            self.add_widget(lbl)
            self.add_widget(check)

        self.search_btn = Button(text="Click me", on_press=self.search_click)
        self.add_widget(self.search_btn)

    def search_click(self, instance):
        search_val = self.search_input.text
        stores = [
            checkbox.filter_val
            for lbl, checkbox in self.checkboxes
            if checkbox.filter_type == "store" and checkbox.state == "down"
        ]

        game_filter = FilterNew(
            name=search_val,
            stores=stores,
        )

        print(api.get_games(game_filter))



class GameDisplayScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        bx1 = BoxLayout(orientation="horizontal")
        l1 = Label(text="bx1")
        l2 = Label(text="bx1")
        bx1.add_widget(l1)
        bx1.add_widget(l2)

        bx2 = BoxLayout(orientation="vertical")
        l3 = Label(text="bx2")
        l4 = Label(text="bx2")
        bx2.add_widget(l3)
        bx2.add_widget(l4)


        self.add_widget(bx1)
        self.add_widget(bx2)


        
        



class MyApp(App):
    def build(self):
        return GameDisplayScreen()


if __name__ == "__main__":
    MyApp().run()
