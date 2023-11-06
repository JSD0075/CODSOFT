from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (450, 600)

class CalculatorLayoutApp(App):
    def build(self):
        self.result = Label(text="", font_size=32,halign="right",  size_hint=(1, 0.2))
        superlayout = BoxLayout(orientation="vertical", spacing=25)
        layout1 = BoxLayout(orientation="vertical")
        layout = GridLayout(cols=4)

        label = Label(text="Calculator Layout")
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for button_text in buttons:
            button = Button(text=button_text, pos_hint={'center_x': 0.5, 'center_y': 0.5},background_color=(1,1,0,1))
            button.bind(on_press=self.on_button_click)
            layout.add_widget(button)

        layout1.add_widget(self.result)
        superlayout.add_widget(layout1)
        superlayout.add_widget(layout)
        return superlayout

    def on_button_click(self, instance):
        current_text = self.result.text

        if instance.text == 'C':
            self.result.text = ''
        elif instance.text == '=':
            try:
                self.result.text = str(eval(current_text))
            except Exception:
                self.result.text = 'Error'
        else:
            self.result.text = current_text + instance.text

CalculatorLayoutApp().run()