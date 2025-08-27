basic.forever(function on_forever() {
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    servos.P1.setStopOnNeutral(false)
    servos.P1.setAngle(90)
    
})
