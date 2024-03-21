from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
MDScreen:

    MDTextField:
        id: field
        pos_hint: {'center_x': .5, 'center_y': .7}
        size_hint_x: None
        width: "200dp"
        hint_text: "Login"
        on_focus: if self.focus: app.menu.open()

    MDTextField:
        id: field
        pos_hint: {'center_x': .5, 'center_y': .6}
        size_hint_x: None
        width: "200dp"
        hint_text: "Password"
        icon_left: "key-variant"
        on_focus: if self.focus: app.menu.open()

    MDRaisedButton:
        id: button
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: "Sing up"
        on_release: app.menu_open()
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "text": f"Item {i}",
                "on_release": lambda x=f"Item {i}": self.set_item(x),
            } for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.field,
            items=menu_items,
            position="bottom",
        )

    def set_item(self, text_item):
        self.screen.ids.field.text = text_item
        self.menu.dismiss()

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"
        return self.screen


Test().run()