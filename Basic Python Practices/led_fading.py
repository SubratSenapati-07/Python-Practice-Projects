import RPi.GPIO as GPIO
import time

LED_PIN = 18  

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)  

try:
    while True:
        
        for duty in range(0, 101, 1):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.01)  

        
        for duty in range(100, -1, -1):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.01)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
