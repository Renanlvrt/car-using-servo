basic.forever(function on_forever() {
    motobit.enable(MotorPower.Off)
})
function on_button_pressed_a() {
    pins.servoWritePin(AnalogPin.P15, 37)
    basic.pause(100)
}

// def logo_is_pressed():
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    pins.servoWritePin(AnalogPin.P15, 160)
    basic.pause(100)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    pins.servoWritePin(AnalogPin.P15, 90)
    basic.pause(100)
    
})
input.logoIsPressed()
input.onButtonPressed(Button.A, on_button_pressed_a)
input.onButtonPressed(Button.A, on_button_pressed_a)
