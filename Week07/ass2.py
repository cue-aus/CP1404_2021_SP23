__author__ = 'Cue'
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.config import Config

class CurrencyConverter(App):

    COUNTRIES = ListProperty(['USA', 'EURO', 'UK', 'CHINA', 'INDIA', 'JAPAN', 'SING'])
    CURRENCY_CODES = ListProperty(['USD', 'EUR', 'GBP', 'CNY', 'INR', 'JPY', 'SGD'])
    BUY_RATES = ListProperty([0.7662, 0.7178, 0.4940, 4.7680, 56.0820, 100.4600, 1.1420])
    SELL_RATES = ListProperty([0.6965, 0.6346, 0.4463, 4.2459, 42.9885, 86.0200, 0.9540])

    title = 'Currency Converter'
    aud_amount = NumericProperty(0.0)
    foreign_amount = NumericProperty(0.0)
    option = StringProperty('FOREIGN -> AUD')
    i = NumericProperty(0)

    def build(self):
        self.root = Builder.load_file('ass2.kv')
        return self.root

    def conversion_option(self, btn):
        btn.state = 'down'
        self.option = btn.text
        self.aud_amount = 0.0
        self.foreign_amount = 0.0
        print(self.option, btn.state)

    def country_option(self, btn):
        btn.state = 'down'
        self.i = self.COUNTRIES.index(btn.text)
        self.root.ids['FOREIGN'].text = self.CURRENCY_CODES[self.i] + ' amount:'
        self.aud_amount = 0.0
        self.foreign_amount = 0.0
        print(self.i, btn.state)

    def recompute1(self, value_str):
        value = float(value_str)
        self.aud_amount = value

        if self.option == 'FOREIGN -> AUD': # buy_rate is applied
            self.foreign_amount = round( self.aud_amount * self.BUY_RATES[self.i], 2 )
        else: # 'A -> F' sell_rate is applied
            self.foreign_amount = round(self.aud_amount * self.SELL_RATES[self.i], 2)

    def recompute2(self, value_str):
        value = float(value_str)
        self.foreign_amount = value

        if self.option == 'FOREIGN -> AUD': # buy_rate is applied
            self.aud_amount = round(self.foreign_amount / self.BUY_RATES[self.i],2)
        else:# 'A -> F' sell_rate is applied
            self.aud_amount = round(self.foreign_amount / self.SELL_RATES[self.i], 2)

Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 400)
CurrencyConverter().run()

