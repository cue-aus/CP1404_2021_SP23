from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class Demo5(App):
    result = StringProperty("hey!")

    def change_pressed(self):
        if self.result == "hey!":
            self.result = "ouch!"
        else:
            self.result = "hey!"

    def build(self):
        self.root = Builder.load_file("demo5.kv")
        return self.root


Demo5().run()

