from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty


class MainWindow(Widget):
    counter = NumericProperty(0)

    def increase(self):
        self.counter += 1


class MyApp(App):
    def build(self):
        return MainWindow()


MyApp().run()
