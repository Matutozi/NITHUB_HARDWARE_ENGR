"""
 Optimize power consumption for a 
battery-powered IoT device by implementing sleep 
modes.

Code that implements the deep sleep functionality
"""

from machine import Pin, lightsleep
import time


pir_pin = Pin(15, Pin.IN, Pin.PULL_DOWN) 
buzzer_pin = Pin(16, Pin.OUT) 

# Initialize buzzer to off
buzzer_pin.value(0)

print("-------SECURITY SYSTEM ACTIVE------------")


time.sleep(30)

try:
    while True:
        if pir_pin.value():
            print("Motion detected! Alarm triggered.")
            buzzer_pin.value(1)
            time.sleep(1)
            buzzer_pin.value(0)
        else:
            print("No motion detected. Entering deep sleep")
            pir_pin.irq(trigger=Pin.IRQ_RISING, wake=machine.DEEPSLEEP)
            lightsleep()

except KeyboardInterrupt:
    print("System Inactive.")
