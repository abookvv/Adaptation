from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivy.factory import Factory
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.relativelayout import MDRelativeLayout

from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivy.lang.builder import Builder
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.widget import Widget
import kivy
from kivy.app import App




class Test(App):
    def build(self):
        return MyGrid()


class MyGrid(Widget):
    diastolic_pressure_info = ObjectProperty(None)

    def calculator(self):
        diastolic = self.diastolic_pressure_info.text
        age = 25
        weight = 60
        height = 170
        pulse = 80
        systolic = 120

        functional_change_index = 0.011 * pulse + 0.014 * systolic + 0.008 * diastolic + 0.014 * age + 0.008 * weight - 0.009 * height - 0.27

        if (functional_change_index < 2.6):
            print(' удовлетворительная адаптация')
        elif (functional_change_index >= 2.6 and functional_change_index <= 3.09):
            print('напряжение механизмов адаптации')
        elif (functional_change_index >= 3.10 and functional_change_index <= 3.49):
            print('неудовлетворительная адаптация')
        elif (functional_change_index >= 3.50):
            print('срыв адаптации')

        print({functional_change_index})

        return functional_change_index

if __name__=="__main__":
    Test().run()
