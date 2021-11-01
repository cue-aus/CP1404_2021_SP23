from kivy.app import App
from kivy.lang import Builder


class Demo3(App):
    def build(self):
        # self.root = Builder.load_file("demo3_eg1.kv")
        # self.root = Builder.load_file("demo3_eg2.kv")
        self.root = Builder.load_file("demo3_eg3.kv")
        return self.root


Demo3().run()

