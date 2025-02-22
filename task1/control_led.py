"""
Python Script that controls and LED using the ldr
This code script turns ON or OFF the led based on a set light treshold

"""

from machine import Pin, ADC
from time import sleep

ldr_pin = 26
led_pin = 15

ldr = ADC(Pin(ldr_pin))
led = Pin(led_pin, Pin.OUT)

print("Smart Home System")

while True:
    
    light_level = ldr.read_u16()
    
    if light_level < 1000:
        led.value(1) 
        print("LED ON")
    else:
        led.value(0)
        print("Idle, Led OFF")
    sleep(0.1)

