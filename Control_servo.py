#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # Importa el módulo RPi.GPIO para controlar los pines GPIO
import time             # Importa el módulo de tiempo para gestionar los retrasos

def AngleToDuty(ang):  # Define una función para convertir el ángulo del servo en ciclo de trabajo
    return float(pos)/10.+5.  # Realiza un cálculo específico para el ciclo de trabajo en función del ángulo

# Configuración del pin del servo como PWM con una frecuencia de 50Hz
servoPin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)

# Configuración de los parámetros del barrido del servo
depart = 0
arrivee = 180
DELAY = 0.1
incStep = 5
pos = depart

if __name__ == '__main__':
    pwm.start(AngleToDuty(pos))  # Inicia el PWM con el ciclo de trabajo inicial

    nbRun = 3
    i = 0
    while i < nbRun:
        print("--------------------------run {}".format(i))  # Muestra el número de ejecución del barrido
        for pos in range(depart, arrivee, incStep):  # Bucle para barrer desde el inicio hasta el final
            duty = AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)  # Cambia el ciclo de trabajo del PWM para mover el servo
            time.sleep(DELAY)           # Espera un tiempo antes de continuar
        print("position: {}° -> duty cycle : {}%".format(pos, duty))  # Muestra la posición y el ciclo de trabajo

        for pos in range(arrivee, depart, -incStep):  # Bucle para barrer desde el final hasta el inicio
            duty = AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)
            time.sleep(DELAY)
        print("position: {}° -> duty cycle : {}%".format(pos, duty))  # Muestra la posición y el ciclo de trabajo

        i = i + 1

    pwm.stop()        # Detiene la señal PWM
    GPIO.cleanup()    # Limpia y libera los pines GPIO
