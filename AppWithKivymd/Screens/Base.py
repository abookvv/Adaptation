from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout


class Screen(Screen):

    def __init__(self, name):
        super().__init__()
        self.name = name
        layout = FloatLayout()
        self.add_widget(layout)