try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    # 其他與GPIO相關的初始化
except ImportError:
    print("RPi.GPIO 模塊未安裝，無法使用 GPIO 功能。")

import time

class GPIOController:
    def __init__(self):
        # 設定 GPIO pin
        self.servo_pwm = 18  # 伺服馬達的 GPIO pin
        self.motor_pin = 17  # 變速馬達的 GPIO pin
        self.motor_pin = 16  # 變速馬達的 GPIO pin

        # 初始化 GPIO
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.servo_pin, GPIO.OUT)
            GPIO.setup(self.motor_pin, GPIO.OUT)
        except NameError:
            print("'GPIO' is not defined")

        # 創建 PWM 對象
        try:
            self.servo_pwm = GPIO.PWM(self.servo_pin, 50)  # 50 Hz 適用於伺服馬達
            self.motor_pwm = GPIO.PWM(self.motor_pin, 1000)  # 1000 Hz 適用於變速馬達
        except NameError:
            print("'GPIO' is not defined")

        # 啟動 PWM
        self.servo_pwm.start(0)
        self.motor_pwm.start(0)


    def turn_left(self):
        self.servo_pwm.ChangeDutyCycle(5)

    def turn_right(self):
        self.servo_pwm.ChangeDutyCycle(10) 

    def speed_up(self):
        self.motor_pwm.ChangeDutyCycle(50)

    def speed_down(self):
        # 控制變速馬達減速
        self.motor_pwm.ChangeDutyCycle(25)  # 調整這個值以達到合適的速度

    def stop_motors(self):
        # 停止 PWM
        self.servo_pwm.stop()
        self.motor_pwm.stop()

        # 釋放 GPIO 資源
        GPIO.cleanup()

    def record_action(self, action):
        # 將動作寫入文件
        with open('actions.txt', 'a') as file:
            file.write(f'{action}\n')

# 使用例子
if __name__ == "__main__":
    gpio_controller = GPIOController()

    try:
        gpio_controller.turn_left()
        time.sleep(2)
        gpio_controller.turn_right()
        time.sleep(2)
        gpio_controller.speed_up()
        time.sleep(2)
        gpio_controller.speed_down()
        time.sleep(2)

    except KeyboardInterrupt:
        gpio_controller.stop_motors()
