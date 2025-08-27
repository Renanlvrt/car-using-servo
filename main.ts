/** 
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

 */
// TURN LEFT: pins.servo_write_pin(AnalogPin.P15, 37)
// TURN RIGHT: pins.servo_write_pin(AnalogPin.P15, 160)
// neutral: pins.servo_write_pin(AnalogPin.P15, 90)
// When it starts:
motobit.enable(MotorPower.Off)
motobit.invert(Motor.Left, true)
motobit.invert(Motor.Right, true)
basic.forever(function on_forever() {
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    pins.servoWritePin(AnalogPin.P15, 90)
    basic.pause(100)
    
})
input.logoIsPressed()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    motobit.enable(MotorPower.On)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 100)
    motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 100)
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        . # # # .
        . . # . .
        `)
    pause(100)
    pins.servoWritePin(AnalogPin.P15, 37)
    motobit.enable(MotorPower.Off)
    pause(15)
    motobit.enable(MotorPower.On)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 60)
    motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 60)
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        . # # # .
        . . # . .
        `)
    pause(100)
})
