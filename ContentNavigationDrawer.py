from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('ContentNavigationDrawer.kv')