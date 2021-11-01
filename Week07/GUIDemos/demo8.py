from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config


class Demo8(App):
    def build(self):
        self.root = Builder.load_file('demo8.kv')
        return self.root


Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 150)
Config.set('graphics', 'resizable', False)
Demo8().run()

