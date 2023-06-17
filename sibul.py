#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpio
import time
import cv2



servo = 14

# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency(servo, 50)

while True:
    print("0 deg")
    pwm.set_servo_pulsewidth(servo, 1300)
    time.sleep(3)

    # print("90 deg")
    # pwm.set_servo_pulsewidth(servo, 1500)
    # time.sleep(3)

    print("180 deg")
    pwm.set_servo_pulsewidth(servo, 1900)
    time.sleep(3)

# turning off servo
pwm.set_PWM_dutycycle(servo, 0)
pwm.set_PWM_frequency(servo, 0)
