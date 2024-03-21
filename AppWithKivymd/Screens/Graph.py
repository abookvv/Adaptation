import matplotlib
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRectangleFlatButton

class GraphScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Graph'
        layout = FloatLayout()
        self.add_widget(layout)

        go_Back = MDRectangleFlatButton(text='Вернуться',
                                        pos_hint={'center_x': .9, 'center_y': .1})
        go_Back.bind(on_press=self.to_main_screen)
        layout.add_widget(go_Back)

    def to_main_screen(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'CalculatorScreen'