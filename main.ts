basic.forever(function on_forever() {
    motobit.enable(MotorPower.Off)
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    pins.servoWritePin(AnalogPin.P15, 90)
    basic.pause(100)
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    pins.servoWritePin(AnalogPin.P15, 180)
    basic.pause(100)
    
})
