from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivy.factory import Factory
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.relativelayout import MDRelativeLayout

from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.gridlayout import GridLayout
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
from kivymd.uix.label import MDLabel

from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem

from data import data


class GraphScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Graph'
        gph_layout = FloatLayout()
        self.add_widget(gph_layout)

        goBack = MDRectangleFlatButton(text='Go to Main screen',
                                        pos_hint={'center_x': .9, 'center_y': .1})
        goBack.bind(on_press=self.to_main_scr)
        gph_layout.add_widget(goBack)

    def to_main_scr(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = "Main"

class InstructionScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Instruction'
        inst_layout = FloatLayout()
        self.add_widget(inst_layout)

        go_Back = MDRectangleFlatButton(text='Go to Main screen',
                                        pos_hint={'center_x': .9, 'center_y': .1})
        go_Back.bind(on_press=self.to_main_screen)
        inst_layout.add_widget(go_Back)

        name_inst = MDFlatButton(text='Instruction',
                           font_size="25sp",
                           pos_hint={'center_x': .5, 'center_y': .8})
        inst_layout.add_widget(name_inst)

        self.why = MDLabel(text=f"Why do you need to use this application?\nnfjnrjngesgnewgksegmkesgnesngsegnkgnseg\n"
                                f"nfjnrjngesgnewgksegmkesgnesngsegnkgnseg\n nfjnrjngesgnewgksegmkesgnesngsegnkgnseg\n nfjnrjngesgnewgksegmkesgnesngsegnkgnseg\n gsrgdrgdrgdrgdrgdrgdrgdrgdrg\nfeefsdfsefsefsefsefsefsefsefsefsefsef\nfsefsefsefsefsefesfesfesfsefsefsefesfsefef\nefsfefsefsefsefsefsefesfesfsefesf",
                               halign="right",
                               pos_hint={'center_x': .3, 'center_y': .6})
        inst_layout.add_widget(self.why)

        self.why_text = MDLabel(text=f".................",
                           halign="right",
                           pos_hint={'center_x': .3, 'center_y': .5})
        inst_layout.add_widget(self.why_text)

        self.how = MDLabel(text="Who to use this application\nУ приложения есть следующий фнкционал",
                           halign="right",
                           pos_hint={'center_x': .3, 'center_y': .4})
        inst_layout.add_widget(self.how)

        self.how_text = MDLabel(text=".....................",
                           halign="right",
                           pos_hint={'center_x': .3, 'center_y': .3})
        inst_layout.add_widget(self.how_text)



    def to_main_screen(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Main'
        return 0


class ProfileScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Profile'
        prf_layout = FloatLayout()
        self.add_widget(prf_layout)

        go_back = MDRectangleFlatButton(text='Go to Main screen',
                                        pos_hint={'center_x': .9, 'center_y': .1})
        go_back.bind(on_press=self.to_main_scr)
        prf_layout.add_widget(go_back)

        inf = MDFlatButton(text='Here your profile info',
                           font_size="25sp",
                           pos_hint={'center_x': .5, 'center_y': .8})
        prf_layout.add_widget(inf)

        self.q_age = MDTextField(hint_text="Input how old are you",
                                 pos_hint={'center_x': .4, 'center_y': .5},
                                 size_hint_x=.4,
                                 width=50,
                                 icon_right="calendar")
        prf_layout.add_widget(self.q_age)

        self.q_weight = MDTextField(hint_text="Input your weight",
                                    pos_hint={'center_x': .4, 'center_y': .4},
                                    size_hint_x=.4,
                                    width=50,
                                    icon_right="weight")
        prf_layout.add_widget(self.q_weight)

        self.q_height = MDTextField(hint_text="Input your height",
                                    pos_hint={'center_x': .4, 'center_y': .3},
                                    size_hint_x=.4,
                                    width=50,
                                    icon_right="human-male-height")
        prf_layout.add_widget(self.q_height)

        save_bt = MDRectangleFlatButton(text='Save',
                                        pos_hint={'center_x': .3, 'center_y': .2})
        save_bt.bind(on_release=self.save_prf)
        prf_layout.add_widget(save_bt)

        self.age_asw = MDLabel(text=f"Your age: {self.q_age.text}",
                               halign="right",
                               pos_hint={'center_x': .3, 'center_y': .5})
        prf_layout.add_widget(self.age_asw)

        self.w_asw = MDLabel(text=f"Your weight: {self.q_weight.text}",
                             halign="right",
                             pos_hint={'center_x': .3, 'center_y': .4})
        prf_layout.add_widget(self.w_asw)

        self.h_asw = MDLabel(text=f"Your height: {self.q_height.text}",
                             halign="right",
                             pos_hint={'center_x': .3, 'center_y': .3})
        prf_layout.add_widget(self.h_asw)

    def to_main_scr(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Main'

    def save_prf(self, instance):
        # if(self.q_age.text):
        if (self.q_age.text.isdigit() == False
                or self.q_weight.text.isdigit() == False
                or self.q_height.text.isdigit() == False):
            dialog = MDDialog(title="Inapptopriate value(s)!\nMake"
                                    " sure you enter only numbers or you fill all fields")
            dialog.open()
        elif (0 > int(self.q_age.text) or int(self.q_age.text) > 150
              or 10 > int(self.q_weight.text) or int(self.q_weight.text) > 300
              or 100 > int(self.q_height.text) or int(self.q_height.text) > 250):
            dialog = MDDialog(title="Inapptopriate value(s)!")
            dialog.open()
        else:
            self.age_asw.text = f"Your age: {self.q_age.text}"
            self.w_asw.text = f"Your weight: {self.q_weight.text}"
            self.h_asw.text = f"Your height: {self.q_height.text}"

            data['age'] = self.q_age.text
            data['weight'] = self.q_weight.text
            data['height'] = self.q_height.text

            self.q_age.text = ''
            self.q_weight.text = ''
            self.q_height.text = ''

            print(data)


class TestScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Test'
        test_layout = FloatLayout()
        self.add_widget(test_layout)

        Go_Back = MDRectangleFlatButton(text='Go to Main screen',
                                        pos_hint={'center_x': .9, 'center_y': .1})
        Go_Back.bind(on_press=self.to_main_scrn)
        test_layout.add_widget(Go_Back)

        q_1 = MDFlatButton(text='Do you smoke cigarettes?',
                           pos_hint={'center_x': .2, 'center_y': .8})
        test_layout.add_widget(q_1)

        self.q_1i = MDTextField(hint_text="Input 'Yes' or 'No'",
                                pos_hint={'center_x': .6, 'center_y': .8},
                                size_hint_x=.4,
                                width=50)
        test_layout.add_widget(self.q_1i)

        q_2 = MDFlatButton(text='Do you use an electronic cigarette or vape?',
                           pos_hint={'center_x': .2, 'center_y': .7})
        test_layout.add_widget(q_2)

        self.q_2i = MDTextField(hint_text="Input 'Yes' or 'No'",
                                pos_hint={'center_x': .6, 'center_y': .7},
                                size_hint_x=.4,
                                width=50)
        test_layout.add_widget(self.q_2i)

        q_3 = MDFlatButton(text='Do you eat healthy?',
                           pos_hint={'center_x': .2, 'center_y': .6})
        test_layout.add_widget(q_3)
        food_bt = MDRectangleFlatButton(text='Choose answer',
                                        pos_hint={'center_x': .6, 'center_y': .6})
        food_bt.bind(on_press=self.food_question)
        test_layout.add_widget(food_bt)

        q_4 = MDFlatButton(text='How often do you do sport?',
                           pos_hint={'center_x': .2, 'center_y': .5})
        test_layout.add_widget(q_4)
        spotr_bt = MDRectangleFlatButton(text='Choose answer',
                                         pos_hint={'center_x': .6, 'center_y': .5})
        spotr_bt.bind(on_press=self.sport_question)
        test_layout.add_widget(spotr_bt)

        q_5 = MDFlatButton(text='Are you following a sleep-wake schedule??',
                           pos_hint={'center_x': .2, 'center_y': .4})
        test_layout.add_widget(q_5)
        s_w_bt = MDRectangleFlatButton(text='Choose answer',
                                       pos_hint={'center_x': .6, 'center_y': .4})
        s_w_bt.bind(on_press=self.sleep_question)
        test_layout.add_widget(s_w_bt)

        q_last = MDFlatButton(text='Do you your type of nervous system?',
                              pos_hint={'center_x': .2, 'center_y': .3})
        test_layout.add_widget(q_last)
        self.q_lasti = MDTextField(hint_text="Input 'Yes' or 'No'",
                                   pos_hint={'center_x': .6, 'center_y': .3},
                                   size_hint_x=.4,
                                   width=50)
        test_layout.add_widget(self.q_lasti)

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

    def to_main_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Main'
        return 0

    def risk_scale(self, *args):
        self.res = 0


class MainScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Main'
        main_layout = FloatLayout()
        self.add_widget(main_layout)

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
        main_layout.add_widget(speed_dial)

        button_res = MDRectangleFlatButton(text="My results",
                                           pos_hint={'center_x': .5, 'center_y': .1},
                                           on_release=self.calculator)

        button_test = MDRectangleFlatButton(text="Test",
                                            pos_hint={'center_x': .3, 'center_y': .8},
                                            on_press=self.to_test_screen)

        button_desc = MDTextButton(text="Please complete a test for more accurate results",
                                   pos_hint={'center_x': .6, 'center_y': .8})

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

        main_layout.add_widget(self.diastolic)
        main_layout.add_widget(self.systolic)
        main_layout.add_widget(self.pulse)

        main_layout.add_widget(button_res)
        main_layout.add_widget(button_test)
        main_layout.add_widget(button_desc)

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
        elif (data['age'] == 0 or data['weight'] == 0 or data['height'] == 0):
            dialog = MDDialog(title="You didn't input data in your profile")
            dialog.open()
        else:
            diastolic = int(self.diastolic.text)
            systolic = int(self.systolic.text)
            pulse = int(self.pulse.text)

            age = int(data['age'])
            weight = int(data['weight'])
            height = int(data['height'])

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

            print(functional_change_index)
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

    def to_test_screen(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = "Test"


class Adaptation(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"
        sm.add_widget(TestScreen())
        sm.add_widget(MainScreen())

        sm.add_widget(ProfileScreen())
        sm.add_widget(InstructionScreen())
        sm.add_widget((GraphScreen()))

        return sm



sm = ScreenManager()

Adaptation().run()