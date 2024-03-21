import datetime
from datetime import *

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton, MDFloatingActionButtonSpeedDial
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from data import User
from datetime import *

user = User()

class CalculatorScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'CalculatorScreen'
        layout = FloatLayout()

        info = MDFlatButton(
            text='Калькулятор ИФИ',
            font_size="30sp",
            pos_hint={'center_x': .5, 'center_y': .8})
        layout.add_widget(info)

        speed_dial = MDFloatingActionButtonSpeedDial(hint_animation=True)
        speed_dial.data = {
            'Account': ['account',
                        "on_press", lambda x: print("pressed account"),
                        'on_release', self.account],
            'Graph': ['graph',
                      "on_press", lambda x: print("pressed graph"),
                      'on_release', self.graph],
            'Instruction': ['instraution',
                      "on_press", lambda x: print("pressed instruction"),
                      'on_release', self.instruction]
        }
        speed_dial.root_button_anim = True
        speed_dial.root_button_anim = True
        layout.add_widget(speed_dial)

        button_res = MDRectangleFlatButton(text="My results",
                                           pos_hint={'center_x': .5, 'center_y': .1},
                                           on_release=self.calculator)

        self.diastolic = MDTextField(hint_text="Write your blood pressure bottom number here",
                                     helper_text="Example: 80",
                                     helper_text_mode="on_focus",
                                     pos_hint={'center_x': .5, 'center_y': .5},
                                     size_hint_x=.7,
                                     width=200,
                                     icon_right="water-plus")

        self.systolic = MDTextField(hint_text="Write your blood pressure top number here",
                                    helper_text="Example: 120",
                                    helper_text_mode="on_focus",
                                    pos_hint={'center_x': .5, 'center_y': .6},
                                    size_hint_x=.7,
                                    width=200,
                                    icon_right="water-plus-outline")

        self.pulse = MDTextField(hint_text="Write your pulse here",
                                 helper_text="Example: 70",
                                 helper_text_mode="on_focus",
                                 pos_hint={'center_x': .5, 'center_y': .4},
                                 size_hint_x=.7,
                                 width=200,
                                 icon_right="clipboard-pulse")

        layout.add_widget(self.diastolic)
        layout.add_widget(self.systolic)
        layout.add_widget(self.pulse)

        layout.add_widget(button_res)

        self.add_widget(layout)

    def calculator(self, obj):
        if (
                self.diastolic.text.isdigit() == False
                or self.systolic.text.isdigit() == False
                or self.pulse.text.isdigit() == False):
            dialog = MDDialog(title="Inapptopriate value(s)!\nMake sure you enter only numbers or you fill all fields")
            dialog.open()
        elif (0 > int(self.diastolic.text) or int(self.diastolic.text) > 300
              or 0 > int(self.systolic.text) or int(self.systolic.text) > 300
              or 0 > int(self.pulse.text) or int(self.pulse.text) > 300):
            dialog = MDDialog(title="Inapptopriate value!\nMake sure you input right numbers")
            dialog.open()

        else:
            diastolic = int(self.diastolic.text)
            systolic = int(self.systolic.text)
            pulse = int(self.pulse.text)

            age = user.age
            weight = user.weight
            height = user.height

            functional_change_index = 0.011 * pulse + 0.014 * systolic + 0.008 \
                                      * diastolic + 0.014 * age + 0.008 \
                                      * weight - 0.009 * height - 0.27

            if (functional_change_index < 2.6):
                print('Удовлетворительная адаптация')
                dialog = MDDialog(title="Удовлетворительная адаптация",
                                  md_bg_color='green',
                                  text=f"{str(functional_change_index)} — your result")
                dialog.open()
            elif (functional_change_index >= 2.6 and functional_change_index <= 3.09):
                print('Напряжение механизмов адаптации')
                dialog = MDDialog(title="Напряжение механизмов адаптации",
                                  md_bg_color=[254/255,199/255,71/255,1],
                                  text=f"{str(functional_change_index)} — your "
                                       f"result\nУ вас увеличивающийся риск обострения"
                                       f" или развития осложнению имеющихся заболеваний")
                dialog.open()
            elif (functional_change_index >= 3.10 and functional_change_index <= 3.49):
                print('Неудовлетворительная адаптация')
                dialog = MDDialog(title="Неудовлетворительная адаптация",
                                  md_bg_color='orange',
                                text=f"{str(functional_change_index)} — your "
                                     f"result\nу вас увеличивающийся риск обострения "
                                     f"или развития осложнению имеющихся заболеваний.\n"
                                     f"Рекомендуется обратитесь к врачу")
                dialog.open()
            elif (functional_change_index >= 3.50):
                print('Срыв адаптации')
                dialog = MDDialog(title="Срыв адаптации", md_bg_color='red',
                                  text=f"{str(functional_change_index)} — your result\nСрочно обратитесь к врачу!")
                dialog.open()

            print(functional_change_index, type(datetime.))
            if user.graghic.create_coords(user.password, datetime.now(), str(functional_change_index)):
                return None # написать окошко что вы уже сегодня измерели ифи
            else:
                return functional_change_index

    def account(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = "Profile"

    def graph(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = "Graph"

    def instruction(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = "Instruction"
