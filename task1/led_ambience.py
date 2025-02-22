"""
micro python code that controls the level of brightness of the led using the ldr
"""

from machine import Pin, PWM, ADC
import time

ldr_pin = 26
led_pin = 15


adc = ADC(Pin(ldr_pin))
led = PWM(Pin(led_pin))

led.freq(1000)  


while True:
    light_level = adc.read_u16()
    scaled_value = light_level // 256

    if scaled_value < 0:
      scaled_value = 0 
    elif scaled_value > 255:
        scaled_value = 255

    brightness = scaled_value
    
    led.duty_u16(brightness * brightness)
    time.sleep(0.5)
