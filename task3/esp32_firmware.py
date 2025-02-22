"""
Task 3: Write firmware for an ESP32 to send sensor 
data (temperature, humidity) to a cloud server via 
MQTT. 

"""
import network
import time
import dht
import machine
from umqtt.simple import MQTTClient


SSID = "Ghebee"
PASSWORD = "**********@11"


AIO_USERNAME = "Matutozi"
AIO_KEY = "-------------------"
MQTT_BROKER = "io.adafruit.com"
MQTT_PORT = 1883


AIO_FEED = f"{AIO_USERNAME}/feeds/temperature_humidity"

dht_pin = 14


dht_sensor = dht.DHT22(machine.Pin(dht_pin))

def connect_wifi():
    """Method that connects the esp32 to the internet
    """
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)

    print(f"WiFi connected! IP: {wlan.ifconfig()[0]}")


def connect_mqtt():
    """Method that connects to the Adafruit server
    """
    client = MQTTClient(AIO_USERNAME, MQTT_BROKER, port=MQTT_PORT, user=AIO_USERNAME, password=AIO_KEY)
    client.connect()
    print("Connected to Adafruit IO MQTT Broker!")
    return client


def publish_sensor_data(client):
    while True:
        try:
            dht_sensor.measure()
            temp = dht_sensor.temperature()
            humidity = dht_sensor.humidity()
            
            
            data = f'{{"temperature": {temp}, "humidity": {humidity}}}'
            

            client.publish(AIO_FEED, data)
            print("Published to Adafruit IO:", data)

        except Exception as e:
            print("Error reading sensor:", e)
        
        time.sleep(5)

try:
    connect_wifi()
    mqtt_client = connect_mqtt()
    publish_sensor_data(mqtt_client)
except KeyboardInterrupt:
    print("Disconnected, stopping script.")
