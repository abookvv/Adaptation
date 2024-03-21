from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from Screens.Registration import RegistrationScreen, RegistrZero, RegistrOne, RegistrTwo, LogInScreen
from Screens.RiskScale import RiskScaleScreen
from Screens.Calculator import CalculatorScreen
from Screens.Profile import ProfileScreen
from Screens.Instruction import InstructionScreen
from Screens.Graph import GraphScreen




class Adaptation(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"

        sm.add_widget(RegistrationScreen())
        sm.add_widget(RegistrZero())
        sm.add_widget(RegistrOne())
        sm.add_widget(RegistrTwo())
        sm.add_widget(RiskScaleScreen())
        sm.add_widget(CalculatorScreen())
        sm.add_widget(LogInScreen())
        sm.add_widget(ProfileScreen())
        sm.add_widget(InstructionScreen())
        sm.add_widget(GraphScreen())

        return sm

sm = ScreenManager()

Adaptation().run()