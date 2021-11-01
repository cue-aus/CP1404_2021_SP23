from kivy.app import App
from kivy.app import Widget


class Demo1(App):
    def build(self):
        self.title = 'hello world!'
        return Widget()


Demo1().run()
