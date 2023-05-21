basic.show_string("Hello!")

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.forever(on_forever)