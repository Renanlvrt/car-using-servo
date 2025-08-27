def on_forever():
    motobit.enable(MotorPower.OFF)
basic.forever(on_forever)

def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P15, 37)
    basic.pause(100)

#def logo_is_pressed():

def on_button_pressed_b():
    pins.servo_write_pin(AnalogPin.P15, 160)
    basic.pause(100)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    pins.servo_write_pin(AnalogPin.P15, 90)
    basic.pause(100)
    pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

input.logo_is_pressed()
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.A, on_button_pressed_a)

