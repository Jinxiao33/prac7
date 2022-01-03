BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'horizontal'
        TextInput:
            id: input_miles
            font_size: 48
            on_text: app.handle_calculate(self.text)
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.25
            Button:
                text: 'Up'
                on_press: app.handle_increment(input_miles.text, 1)
            Button:
                text: 'Down'
                on_press: app.handle_increment(input_miles.text, -1)
#    Button:
#        text: 'Convert m to km'
#        on_press: app.handle_calculate()
    Label:
        id: output_label
        text: app.output_km
        font_size: 48
        color: (1, 1, 0, 1)