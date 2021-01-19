from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder

Builder.load_file("./QuarkGUI/Inputs/Inputs.kv")


class SearchInput(TextInput):
    pass


class FromPriceInput(TextInput):
    pass


class ToPriceInput(TextInput):
    pass
