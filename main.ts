control.onEvent(EventBusSource.MICROBIT_ID_IO_P16, EventBusValue.MICROBIT_PIN_EVT_RISE, function on_microbit_id_io_p16_pin_evt_rise() {
    
    item += 1
    basic.pause(100)
})
let item = 0
pins.setEvents(DigitalPin.P16, PinEventType.Edge)
basic.forever(function on_forever() {
    
    if (item == 0) {
        pins.analogWritePin(AnalogPin.P0, 1023)
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P2, 0)
    } else if (item == 1) {
        pins.analogWritePin(AnalogPin.P0, 0)
        pins.analogWritePin(AnalogPin.P1, 1023)
        pins.analogWritePin(AnalogPin.P2, 0)
    } else if (item == 2) {
        pins.analogWritePin(AnalogPin.P0, 0)
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P2, 1023)
    } else {
        item = 0
    }
    
})
