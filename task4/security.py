"""
Task 4: Implement a security feature using a PIR 
motion sensor to trigger an alarm when motion is 
detected
"""

from machine import Pin
import time



pir_pin = Pin(15, Pin.IN)
buzzer_pin = Pin(16, Pin.OUT) 

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
            print("No motion detected.")
            buzzer_pin.value(0)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("System Inactive.")