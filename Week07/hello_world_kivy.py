from kivy.app import App
from kivy.app import Widget


class HelloWorld(App):
    def build(self):
        self.root = Widget()
        self.title = 'Hello World from Cue'
        return self.root


HelloWorld().run()
