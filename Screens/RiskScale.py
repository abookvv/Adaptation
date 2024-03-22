from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog


class RiskScaleScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = "RiskScaleScreen"
        layout = FloatLayout()


        q_1 = MDFlatButton(text='Курите ли вы?',
                           pos_hint={'center_x': .2, 'center_y': .8})
        layout.add_widget(q_1)

        self.q_1i = MDTextField(hint_text="Введите да или нет",
                                pos_hint={'center_x': .8, 'center_y': .8},
                                size_hint_x=.4,
                                width=50)
        layout.add_widget(self.q_1i)

        q_2 = MDFlatButton(text='Импользуете ли вы электонные сигареты или вейп?',
                           pos_hint={'center_x': .2, 'center_y': .7})
        layout.add_widget(q_2)

        self.q_2i = MDTextField(hint_text="Введите да или нет'",
                                pos_hint={'center_x': .8, 'center_y': .7},
                                size_hint_x=.4,
                                width=50)
        layout.add_widget(self.q_2i)

        q_3 = MDFlatButton(text='На сколько сбалансированно вы писаетесь?',
                           pos_hint={'center_x': .2, 'center_y': .6})
        layout.add_widget(q_3)
        food_bt = MDRectangleFlatButton(text='Выберите ответ',
                                        pos_hint={'center_x': .8, 'center_y': .6})
        food_bt.bind(on_press=self.food_question)
        layout.add_widget(food_bt)

        q_4 = MDFlatButton(text='Как часто вы занисаетесь спортом?',
                           pos_hint={'center_x': .2, 'center_y': .5})
        layout.add_widget(q_4)
        spotr_bt = MDRectangleFlatButton(text='Выберите ответ',
                                         pos_hint={'center_x': .8, 'center_y': .5})
        spotr_bt.bind(on_press=self.sport_question)
        layout.add_widget(spotr_bt)

        q_5 = MDFlatButton(text='Придерживаетест ли вы режима \nзасыпания и пробуждения?',
                           pos_hint={'center_x': .2, 'center_y': .4})#Are you following a sleep-wake schedule
        layout.add_widget(q_5)
        s_w_bt = MDRectangleFlatButton(text='Выберите ответ',
                                       pos_hint={'center_x': .8, 'center_y': .4})
        s_w_bt.bind(on_press=self.sleep_question)
        layout.add_widget(s_w_bt)

        q_last = MDFlatButton(text='Знаете ли вы свой тип \nнервной системы?',
                              pos_hint={'center_x': .2, 'center_y': .3})
        layout.add_widget(q_last)
        self.q_lasti = MDTextField(hint_text="Выберите ответ",
                                   pos_hint={'center_x': .6, 'center_y': .3},
                                   size_hint_x=.4,
                                   width=50)
        layout.add_widget(self.q_lasti)


        self.add_widget(layout)

    def sport_question(self, *args):
        self.dialog = MDDialog(title="How often do you do sport?",
                          type="confirmation",
                          buttons=[
                              MDFlatButton(
                                  text="Discard",
                                  on_release=self.close_dialog,
                                  theme_text_color="Custom"),
                              MDRaisedButton(
                                  text="Apply",
                                  theme_text_color="Custom")]
                          )
        self.dialog.open()

    def food_question(self, *args):
        self.dialog = MDDialog(title="How often do you do sport?",
                               type="confirmation",
                               buttons=[
                                   MDFlatButton(
                                       text="Discard",
                                       on_release=self.close_dialog,
                                       theme_text_color="Custom"),
                                   MDRaisedButton(
                                       text="Apply",
                                       theme_text_color="Custom")]
                               )
        self.dialog.open()

    def sleep_question(self, *args):
        self.dialog = MDDialog(title="How often do you do sport?",
                               type="confirmation",
                               buttons=[
                                   MDFlatButton(
                                       text="Discard",
                                       on_release=self.close_dialog,
                                       theme_text_color="Custom"),
                                   MDRaisedButton(
                                       text="Apply",
                                       theme_text_color="Custom")]
                               )
        self.dialog.open()

    def close_dialog(self, odj):
        self.dialog.dismiss()
