from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivy.factory import Factory
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.relativelayout import MDRelativeLayout

from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRaisedButton, \
    MDRectangleFlatButton, MDTextButton, MDFloatingActionButtonSpeedDial
from kivy.lang.builder import Builder
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

from buttons import dias, syst, heart_rate, age, weight, height

# screen_test = '''
# ScreenManager:
#     TestScreen:
#
# <TestScreen>:
#     name: 'test'
#     MDLabel:
#         text: 'Answer some questions, please'
#         halign: 'center'
# '''


class Adaptation(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"

        speed_dial = MDFloatingActionButtonSpeedDial(hint_animation=True)
        speed_dial.data = {
            'Account': ['account',
                        "on_press", lambda x: print("pressed account"),
                        'on_release', self.account]
        }
        speed_dial.root_button_anim = True
        screen.add_widget(speed_dial)

        button_res = MDRectangleFlatButton(text="My results",
                                           pos_hint={'center_x': .5, 'center_y': .1},
                                           on_release=self.calculator)

        button_test = MDRectangleFlatButton(text="Test",
                                            pos_hint={'center_x': .3, 'center_y': .8})

        button_desc = MDTextButton(text="Please complete a test for more accurate results",
                                   pos_hint={'center_x': .6, 'center_y': .8})

        self.diastolic = Builder.load_string(dias)
        screen.add_widget(self.diastolic)

        self.systolic = Builder.load_string(syst)
        screen.add_widget(self.systolic)

        self.pulse = Builder.load_string(heart_rate)
        screen.add_widget(self.pulse)

        self.age = Builder.load_string(age)
        screen.add_widget(self.age)

        self.weight = Builder.load_string(weight)
        screen.add_widget(self.weight)

        self.height = Builder.load_string(height)
        screen.add_widget(self.height)

        screen.add_widget(button_res)
        screen.add_widget(button_test)
        screen.add_widget(button_desc)

        return screen

    def calculator(self, obj):
        print(self.diastolic.text, ' - diastolic pressure')
        print(self.systolic.text, ' - systolic pressure')
        print(self.pulse.text, ' - pulse')
        print(self.age.text, ' - age')
        print(self.height.text, ' - height')
        print(self.weight.text, ' - weight')

        diastolic = int(self.diastolic.text)
        systolic = int(self.systolic.text)
        pulse = int(self.pulse.text)
        age = int(self.age.text)
        weight = int(self.weight.text)
        height = int(self.height.text)

        functional_change_index = 0.011 * pulse + 0.014 * systolic + 0.008 \
                                  * diastolic + 0.014 * age + 0.008 \
                                  * weight - 0.009 * height - 0.27

        if (functional_change_index < 2.6):
            print(' удовлетворительная адаптация')
        elif (functional_change_index >= 2.6 and functional_change_index <= 3.09):
            print('напряжение механизмов адаптации')
        elif (functional_change_index >= 3.10 and functional_change_index <= 3.49):
            print('неудовлетворительная адаптация')
        elif (functional_change_index >= 3.50):
            print('срыв адаптации')

        print(functional_change_index)
        return functional_change_index

    def account(self, *args):
        print(args)
        print('account')

    def to_test_screen(self, *args):
        pass
        # self.manager.current = "Test"

class TestScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Test'
        second_layout = FloatLayout()
        self.add_widget(second_layout)


# sm = ScreenManager()
# sm.add_widget(TestScreen(name='test'))

Adaptation().run()
