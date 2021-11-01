from kivy.app import App
from kivy.lang import Builder


class Demo7(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message = 'ouch!!'

    def build(self):
        self.root = Builder.load_file('demo7.kv')
        return self.root

    def button_pressed(self):
        print(self.message)


Demo7().run()

