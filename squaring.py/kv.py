BoxLayout:
    orientation: 'vertical'
    TextInput:
        id: input_number
        text: '7'
        font_size: 48
        multiline: False
    Button:
        text: 'Square'
        # the following line specifies the function in the app class to call when the button is pressed
        on_press: app.handle_calculate(input_number.text)
    Label:
        id: output_label
        font_size: 48
        color: (0, 1, 1, 1)