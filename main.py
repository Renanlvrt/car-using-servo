def on_forever():
    pass
basic.forever(on_forever)
def on_button_pressed_a():
    servos.P1.set_stop_on_neutral(False)
    servos.P1.set_angle(90)
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)