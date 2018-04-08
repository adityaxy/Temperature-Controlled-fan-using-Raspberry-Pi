import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Fan = 7
GPIO.setup(Fan, GPIO.OUT)

sensor = Adafruit_DHT.AM2302

humidity, temperature = Adafruit_DHT.read_retry(sensor,4)   #Pin 4 IS IN BCM Mode.

print ("Temperature = %s , Humidity = %s" % temperature, humidity)

try:
    if temperature > 20:
        print("Temperature is greater than 20 degree.")
        GPIO.output(Fan,0)
        print("Fan is ON.")
        sleep(10)
        GPIO.output(Fan,1)
    else:
        GPIO.output(Fan,1)
        print("Temperature is Less than 20 degree.")
finally:
    GPIO.cleanup()
