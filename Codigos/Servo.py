import RPi.GPIO as GPIO
import time

class Servo:
    
    __motor: GPIO.PWM
    __pin: int
    __home: float = 7.5

    def __init__(self, motorPin, frequency = 50):
        self.__pin = motorPin
        GPIO.setmode (GPIO.BCM)
        GPIO.setup(motorPin,GPIO.OUT) # inicializar GPIO19 como salida
        self.__motor = GPIO.PWM(motorPin, frequency)
        self.__motor.start(self.__home)
        time.sleep(2)

    def move(self, angle):
        self.__motor.ChangeDutyCycle((angle+45.0)/18.0)
        
    
    def getPin(self) :
        return self.__pin

    def stop(self):
        self.__motor.stop()
