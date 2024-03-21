from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from data import User


user = User()

class InstructionScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Instruction'
        inst_layout = FloatLayout()
        self.add_widget(inst_layout)

        go_Back = MDRectangleFlatButton(text='Вернуться',
                                        pos_hint={'center_x': .9, 'center_y': .1})
        go_Back.bind(on_press=self.to_main_screen)
        inst_layout.add_widget(go_Back)

        name_inst = MDFlatButton(text='Instruction',
                           font_size="25sp",
                           pos_hint={'center_x': .5, 'center_y': .8})
        inst_layout.add_widget(name_inst)

        self.why = MDLabel(text=f"Что такое ИФИ и зачем его измерять?",
                               halign="right",
                               pos_hint={'center_x': .3, 'center_y': .6})
        inst_layout.add_widget(self.why)

        self.why_text = MDLabel(text=f"Индекс функциональных изменений поможет понять, \n"
                                     f"не развиваются ли у вас какие-либо хронические заболевания.\n"
                                     f" Измерять ИФИ для наиболее точного результата необходимо с \n"
                                     f"спокойном сидячем состоянии. Рекомендуется делать это раз в неделю. \n"
                                     f"Тенденцию изменения ИФИ вы сможете найти в разделе «Статистика»",
                           halign="right",
                           pos_hint={'center_x': .3, 'center_y': .5})
        inst_layout.add_widget(self.why_text)

        self.how = MDLabel(text="Как пользоваться приложением?",
                           halign="right",
                           pos_hint={'center_x': .3, 'center_y': .4})
        inst_layout.add_widget(self.how)

        self.how_text = MDLabel(text="В этом приложении можно измерить свой уровень ИФИ \n"
                                     "с помощью данных о давлении и пульсе, который необходимо\n"
                                     "измерить самостоятельно. Далее приложение даст результат \n"
                                     "и его описания с рекомендациями.",
                           halign="right",
                           pos_hint={'center_x': .3, 'center_y': .3})
        inst_layout.add_widget(self.how_text)



    def to_main_screen(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'CalculatorScreen'