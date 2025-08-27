"""
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
"""
#TURN LEFT: pins.servo_write_pin(AnalogPin.P15, 37)
#TURN RIGHT: pins.servo_write_pin(AnalogPin.P15, 160)
#neutral: 90

#When it starts:
motobit.enable(MotorPower.OFF)

def on_forever():
    motobit.enable(MotorPower.OFF)
basic.forever(on_forever)

def on_button_pressed_a():
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)
    basic.pause(500)
    motobit.enable(MotorPower.OFF)
    pins.servo_write_pin(AnalogPin.P15, 37)
    basic.pause(100)
    motobit.enable(MotorPower.OFF)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
    basic.pause(100)
    motobit.enable(MotorPower.OFF)

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