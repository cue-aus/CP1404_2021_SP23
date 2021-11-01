from kivy.app import App
from kivy.lang import Builder


class Demo4(App):
    def change_pressed(self):
        if self.root.ids['result'].text == "hey!":
            self.root.ids['result'].text = "ouch!"
        else:
            self.root.ids['result'].text = "hey!"

    def build(self):
        self.root = Builder.load_file("demo4.kv")
        return self.root


Demo4().run()

