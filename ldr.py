#!/usr/loca/bin/python
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

    #define the pin
pin_to_circuit = 7
client = mqtt.Client()

# user name has to be called before connect - my notes.
client.username_pw_set("yojlxbnf", "0Qjl0D8bKR-v")
client.connect('tailor.cloudmqtt.com', 16255, 60)
client.loop_start()
client.subscribe ("sistemEmbedded" ,0 )

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print(rc_time(pin_to_circuit))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
