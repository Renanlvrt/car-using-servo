def on_forever():
    motobit.enable(MotorPower.OFF)
    pass
basic.forever(on_forever)

def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P15, 90)
    basic.pause(100)
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.servo_write_pin(AnalogPin.P15, 180)
    basic.pause(100)
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)