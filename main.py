def on_microbit_id_io_p16_pin_evt_rise():
    global item
    item += 1
    basic.pause(100)
control.on_event(EventBusSource.MICROBIT_ID_IO_P16,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_io_p16_pin_evt_rise)

item = 0
pins.set_events(DigitalPin.P16, PinEventType.EDGE)

def on_forever():
    global item
    if item == 0:
        pins.analog_write_pin(AnalogPin.P0, 1023)
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P2, 0)
    elif item == 1:
        pins.analog_write_pin(AnalogPin.P0, 0)
        pins.analog_write_pin(AnalogPin.P1, 1023)
        pins.analog_write_pin(AnalogPin.P2, 0)
    elif item == 2:
        pins.analog_write_pin(AnalogPin.P0, 0)
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P2, 1023)
    else:
        item = 0
basic.forever(on_forever)
