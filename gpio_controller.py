import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# 其他與GPIO相關的初始化
import time

class GPIOController:
    def __init__(self):
        self.in1=22#I/O
        self.in2=23
        self.in3=24
        self.in4=25
        self.ena1=12#PWM
        self.enb1=13
        self.ena2=26
        self.enb2=27
        self.servo=5
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.ena1,GPIO.OUT)
        GPIO.setup(self.enb1,GPIO.OUT)
        GPIO.setup(self.ena2,GPIO.OUT)
        GPIO.setup(self.enb2,GPIO.OUT)
        GPIO.setup(self.servo,GPIO.OUT)

        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)

        self.servo_pwm = GPIO.PWM(self.servo, 50)
        self.motor_pwm1 = GPIO.PWM(self.ena1, 1000)
        self.motor_pwm2 = GPIO.PWM(self.enb1, 1000)
        self.motor_pwm3 = GPIO.PWM(self.ena2, 1000)
        self.motor_pwm4 = GPIO.PWM(self.enb2, 1000)
        self.servo_pwm.start(0)
        self.motor_pwm1.start(0)
        self.motor_pwm2.start(0)
        self.motor_pwm3.start(0)
        self.motor_pwm4.start(0)
    def Forward(self):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.HIGH)

    def turn_change(self,x):
        self.servo_pwm.ChangeDutyCycle(x)#1-50
    def speed_change(self,x):
        self.motor_pwm1.ChangeDutyCycle(x)#1-1000
        self.motor_pwm2.ChangeDutyCycle(x)
        self.motor_pwm3.ChangeDutyCycle(x)
        self.motor_pwm4.ChangeDutyCycle(x)
    def stop_motors(self):
        self.servo_pwm.stop()
        self.motor_pwm1.stop()
        self.motor_pwm2.stop()
        self.motor_pwm3.stop()
        self.motor_pwm4.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    gpio_controller = GPIOController()
