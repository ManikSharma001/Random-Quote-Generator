'''
            Quotes App
=========================================
This program generates a random quote everything time the user requests by pressing a button. Uses the Kivy framework. This special version uses webscraping technology in order to obtain the quotes. 
'''
#Things to Add: Export it to Play Store, add a way to maxmize window automatically, etc. 

import random as r
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
import scrape

class quotesApp(App):
    def build(self):
        Window.clearcolor = (0.98, 0.28, 1, 1)
        main_layout = FloatLayout(size = (500, 500))
        self.welcome = Label(text = "The Most Wonderful Quotes of All-Time!", pos_hint = {"x" : .018, "y": .41}, font_size = '40sp', color =(1, 1, 1, 1), markup = True,)
        main_layout.add_widget(self.welcome)
        self.quote = TextInput(multiline = "True", readonly = True, halign = "center", font_size=50, size_hint = (.71,.55),
                               pos_hint = {"x": .15,"y": .30},background_color = (0.98, 0.28, 1, 1)) 
        main_layout.add_widget(self.quote)
        self.author = TextInput(multiline = "False", readonly = True, halign = "center", font_size = 25, size_hint = (.43, .10), pos_hint = {"x": .285,"y": .175},
                                background_color = (0.98, 0.28, 1, 1))
        main_layout.add_widget(self.author)
        nextButton = Button(text = "Click for a Quote", size_hint = (.3, .1), pos_hint = {"x": .355, "y": .055}, background_color = (0.98, 0.28, 1, 1))
        nextButton.bind(on_press = self.onButtonPress)
        main_layout.add_widget(nextButton)

        return main_layout

    def onButtonPress(self, instance):
        quotesNAuthors = scrape.quotes_and_authors
        for i in range(1):
            authors, quotes = r.choice(list(quotesNAuthors.items()))
            self.quote.text = ' "' + quotes + ' " '
            self.author.text = " - " + authors
            return quotes, authors
        


if __name__ == '__main__':
    app = quotesApp()
    app.run()
