from kivy.app import App
from kivy.lang import Builder


class Demo6(App):
    def build(self):
        # self.root = Builder.load_file('demo6_box.kv')
        # self.root = Builder.load_file('demo6_grid.kv')
        self.root = Builder.load_file('demo6_float.kv')
        return self.root


Demo6().run()
