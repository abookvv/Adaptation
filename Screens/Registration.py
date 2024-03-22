from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from data import user



class RegistrationScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = "Registration"
        layout = FloatLayout()

        inf = MDFlatButton(text='Добро пожаловать',
                           font_size="30sp",
                           pos_hint={'center_x': .5, 'center_y': .7})
        layout.add_widget(inf)

        button_registr = MDRectangleFlatButton(text='Register',
                                 font_size="25sp",
                                 pos_hint={'center_x': .5, 'center_y': .4})
        button_registr.bind(on_press=self.on_button_registr)
        layout.add_widget(button_registr)

        button_login = MDRectangleFlatButton(text='Log in',
                                 font_size="25sp",
                                 pos_hint={'center_x': .5, 'center_y': .3})
        layout.add_widget(button_login)
        button_login.bind(on_press=self.on_button_login)

        self.add_widget(layout)

    def on_button_registr(self, *args):
        self.manager.transition.direction = 'up'
        self.manager.current = "RegistrZero"

    def on_button_login(self, *args):
        self.manager.transition.direction = 'up'
        self.manager.current = "LogInScreen"


class RegistrZero(Screen):
    def __init__(self):
        super().__init__()
        self.name = "RegistrZero"
        layout = FloatLayout()

        inf = MDFlatButton(text='Введите email и пароль',
                           font_size="25sp",
                           pos_hint={'center_x': .5, 'center_y': .8})
        layout.add_widget(inf)

        self.button_password = MDTextField(hint_text="Придумайте пароль из 6 цифр",
                                           pos_hint={'center_x': .4, 'center_y': .6},
                                           size_hint_x=.4,
                                           width=50,
                                           icon_right="lock")
        layout.add_widget(self.button_password)

        self.button_email = MDTextField(hint_text="Введите вашу почту: ***@gmail.com",
                                        pos_hint={'center_x': .4, 'center_y': .5},
                                        size_hint_x=.4,
                                        width=50,
                                        icon_right="email")
        layout.add_widget(self.button_email)

        save_bt = MDRectangleFlatButton(text='Save',
                                        pos_hint={'center_x': .3, 'center_y': .2})
        save_bt.bind(on_release=self.save_password)
        layout.add_widget(save_bt)

        self.add_widget(layout)

    def save_password(self, *args):
        if self.button_password.text.isdigit() == True and len(self.button_password.text) == 6:
            user.password = self.button_password.text
            user.email = self.button_email.text
            print(user.password)

            self.manager.transition.direction = 'up'
            self.manager.current = "RegistrOne"
        else:
            dialog = MDDialog(title="Вы ввели что-то неправильно!")
            dialog.open()


class RegistrOne(Screen):
    def __init__(self):
        super().__init__()
        self.name = "RegistrOne"
        layout = FloatLayout()

        inf = MDFlatButton(text='Введите свои личные данные',
                           font_size="25sp",
                           pos_hint={'center_x': .5, 'center_y': .8})
        layout.add_widget(inf)

        self.button_age = MDTextField(hint_text="Введите ваш возраст",
                                 pos_hint={'center_x': .4, 'center_y': .6},
                                 size_hint_x=.4,
                                 width=50,
                                 icon_right="calendar")
        layout.add_widget(self.button_age)

        self.button_weight = MDTextField(hint_text="Введите ваш вес",
                                    pos_hint={'center_x': .4, 'center_y': .5},
                                    size_hint_x=.4,
                                    width=50,
                                    icon_right="weight")
        layout.add_widget(self.button_weight)

        self.button_height = MDTextField(hint_text="Введите ваш рост",
                                    pos_hint={'center_x': .4, 'center_y': .4},
                                    size_hint_x=.4,
                                    width=50,
                                    icon_right="human-male-height")
        layout.add_widget(self.button_height)

        save_bt = MDRectangleFlatButton(text='Сохранить',
                                        pos_hint={'center_x': .3, 'center_y': .2})
        save_bt.bind(on_release=self.save_persData)
        layout.add_widget(save_bt)

        self.add_widget(layout)

    def save_persData(self, *args):
        if (self.button_age.text.isdigit() == False
                or self.button_weight.text.isdigit() == False
                or self.button_height.text.isdigit() == False):
            dialog = MDDialog(title="Вы ввели что-то неправильно!")
            dialog.open()
        elif (0 > int(self.button_age.text) or int(self.button_age.text) > 150
              or 10 > int(self.button_weight.text) or int(self.button_weight.text) > 300
              or 100 > int(self.button_height.text) or int(self.button_height.text) > 250):
            dialog = MDDialog(title="Inapptopriate value(s)!")
            dialog.open()
        else:
            user.age = self.button_age.text
            user.weight = self.button_weight.text
            user.height = self.button_height.text

            print(user.age,user.weight,user.height)
            user.create()
            self.manager.transition.direction = 'up'
            self.manager.current = "RegistrTwo"


class RegistrTwo(Screen):
    def __init__(self):
        super().__init__()
        self.name = "RegistrTwo"
        layout = FloatLayout()

        inf = MDFlatButton(text='Ответьте на вопросы "Шкалы риска"',
                           font_size="30sp",
                           pos_hint={'center_x': .5, 'center_y': .8})
        layout.add_widget(inf)

        info = MDFlatButton(text='Это займет всего пару минут, а результаты \nпомогут создать более персонализированный подход',
                           font_size="23sp",
                           pos_hint={'center_x': .5, 'center_y': .6})
        layout.add_widget(info)

        button_yes = MDRectangleFlatButton(text='Пройти',
                                        pos_hint={'center_x': .4, 'center_y': .2})
        button_yes.bind(on_release=self.go_to_riskscale)
        layout.add_widget(button_yes)

        button_no = MDRectangleFlatButton(text='Не сейчас',
                                        pos_hint={'center_x': .6, 'center_y': .2})
        button_no.bind(on_release=self.go_to_main)
        layout.add_widget(button_no)

        self.add_widget(layout)

    def go_to_riskscale(self, *args):
        self.manager.transition.direction = 'up'
        self.manager.current = "RiskScaleScreen"

    def go_to_main(self, *args):
        self.manager.transition.direction = 'up'
        self.manager.current = "CalculatorScreen"


class LogInScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = "LogInScreen"
        layout = FloatLayout()

        inf = MDFlatButton(text='Введите пароль',
                           font_size="25sp",
                           pos_hint={'center_x': .5, 'center_y': .8})
        layout.add_widget(inf)

        self.password_chec = MDTextField(hint_text="Введите пароль",
                                         pos_hint={'center_x': .4, 'center_y': .6},
                                         size_hint_x=.4,
                                         width=50,
                                         icon_right="lock")
        layout.add_widget(self.password_chec)

        password_checker = MDRectangleFlatButton(text='Проверить',
                                                 pos_hint={'center_x': .3, 'center_y': .2})
        password_checker.bind(on_release=self.password_check)
        layout.add_widget(password_checker)

        goBack = MDRectangleFlatButton(text='Вернуться',
                                       pos_hint={'center_x': .7, 'center_y': .2})
        goBack.bind(on_press=self.to_start)
        layout.add_widget(goBack)

        self.add_widget(layout)

    def to_start(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = "Registration"

    def password_check(self, *args):
        user.password = self.password_chec.text
        if user.check_props():
            print(user.password)
            self.manager.transition.direction = 'up'
            self.manager.current = "CalculatorScreen"
        else:
            dialog = MDDialog(title="Неверный пароль")
            dialog.open()
