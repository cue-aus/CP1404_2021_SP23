from kivy.app import App
from kivy.lang import Builder


class Demo2(App):
    def build(self):
        self.root = Builder.load_file("demo2.kv")
        return self.root


Demo2().run()
