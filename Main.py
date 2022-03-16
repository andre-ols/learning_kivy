from kivymd.app import MDApp
from kivy.lang import Builder
import ContentNavigationDrawer as content

class Main(MDApp):
    def build(self):
        content.ContentNavigationDrawer()
        # return Builder.load_file('Main.kv') 

Main().run()
