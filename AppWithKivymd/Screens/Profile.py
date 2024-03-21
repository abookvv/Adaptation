from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

from data import user

class ProfileScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Profile'
        layout = FloatLayout()
        self.add_widget(layout)

        go_back = MDRectangleFlatButton(text='Вернуться на главный экран',
                                        pos_hint={'center_x': .7, 'center_y': .1})
        go_back.bind(on_press=self.to_main_scr)
        layout.add_widget(go_back)

        inf = MDFlatButton(text='Here your profile info',
                           font_size="25sp",
                           pos_hint={'center_x': .5, 'center_y': .8})
        layout.add_widget(inf)

        self.q_age = MDTextField(hint_text="Введите ваш возраст",
                                 pos_hint={'center_x': .4, 'center_y': .5},
                                 size_hint_x=.4,
                                 width=50,
                                 icon_right="calendar")
        layout.add_widget(self.q_age)

        self.q_weight = MDTextField(hint_text="Введите ваш вес",
                                    pos_hint={'center_x': .4, 'center_y': .4},
                                    size_hint_x=.4,
                                    width=50,
                                    icon_right="weight")
        layout.add_widget(self.q_weight)

        self.q_height = MDTextField(hint_text="Введите ваш рост",
                                    pos_hint={'center_x': .4, 'center_y': .3},
                                    size_hint_x=.4,
                                    width=50,
                                    icon_right="human-male-height")
        layout.add_widget(self.q_height)

        save_bt = MDRectangleFlatButton(text='Сохранить',
                                        pos_hint={'center_x': .3, 'center_y': .2})
        save_bt.bind(on_release=self.save_prf)
        layout.add_widget(save_bt)

        self.age_asw = MDLabel(text=f"Ваш возраст: {user.age}",
                               halign="right",
                               pos_hint={'center_x': .3, 'center_y': .5})
        layout.add_widget(self.age_asw)

        self.w_asw = MDLabel(text=f"Ваш вес: {user.weight}",
                             halign="right",
                             pos_hint={'center_x': .3, 'center_y': .4})
        layout.add_widget(self.w_asw)

        self.h_asw = MDLabel(text=f"Ваш рост: {user.height}",
                             halign="right",
                             pos_hint={'center_x': .3, 'center_y': .3})
        layout.add_widget(self.h_asw)

        change_lahguage = MDRectangleFlatButton(text='Изменить язык интерфейса',
                                        pos_hint={'center_x': .3, 'center_y': .7})
        change_lahguage.bind(on_release=self.change_lahguage_func)
        layout.add_widget(change_lahguage)

        change_password = MDRectangleFlatButton(text='Изменить пароль',
                                                pos_hint={'center_x': .3, 'center_y': .6})
        change_password.bind(on_release=self.change_password_func)
        layout.add_widget(change_password)

    def change_lahguage_func(self, *args):
        dialog = MDDialog(title="Выберите язык")
        dialog.open()

    def change_password_func(self, *args):
        pass

    def to_main_scr(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'CalculatorScreen'

    def save_prf(self, instance):
        user = User.current_user
        if (self.q_age.text.isdigit() == False
                or self.q_weight.text.isdigit() == False
                or self.q_height.text.isdigit() == False):
            dialog = MDDialog(title="Неверные значения!")
            dialog.open()
        elif (0 > int(self.q_age.text) or int(self.q_age.text) > 150
              or 10 > int(self.q_weight.text) or int(self.q_weight.text) > 300
              or 100 > int(self.q_height.text) or int(self.q_height.text) > 250):
            dialog = MDDialog(title="Неверные значения!")
            dialog.open()
        else:
            self.age_asw.text = f"Your age: {self.q_age.text}"
            self.w_asw.text = f"Your weight: {self.q_weight.text}"
            self.h_asw.text = f"Your height: {self.q_height.text}"

            user.age = self.q_age.text
            user.weight = self.q_weight.text
            user.height = self.q_height.text

            self.q_age.text = ''
            self.q_weight.text = ''
            self.q_height.text = ''

