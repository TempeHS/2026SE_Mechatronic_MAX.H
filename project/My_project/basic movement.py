import time 
import PiicoDev_Ultrasonic
from basicmovement import Movementsubsystem

#create two servo objects
Left_servo = Servo(pwm=16, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
Right_servo = Servo(pwm=16, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

class Basic_movement():
    def __init(self, Right_servo, Left_servo):
        self.Left_servo = Left_servo
        self.Right_servo = Right_servo

    def Turn_right(self):
        self.Right_servo.set_duty(2000)
        self.Left_servo.set_duty(1500)

    def Turn_left(self):
        self.Right_servo.set_duty(1500)
        self.Left_servo.set_duty(2000)

    #use with caution
    def Basic_backward(self):
        self.Right_servo.set_duty(1000)
        self.Left_servo.set_duty(1000)

    def basic_forward(self):
        self.Right_servo.set_duty(2000)
        self.Left_servo.set_duty(2000)