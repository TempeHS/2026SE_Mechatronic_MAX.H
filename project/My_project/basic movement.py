import time 
import PiicoDev_Ultrasonic
from servo import Servo
from PID_Controller import PIDControl

class Basic_movement(Servo):
    def __init__(self, Right_servo, Left_servo):
        self.Left_servo = Servo(pwm=servo_pwm, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
        self.Right_servo = Servo(pwm=servo_pwm, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

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

class Ultra_sensor_states(PiicoDev_Ultrasonic):
    def __init__(self, range_a, range_b)
        self.range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
    
    def Forward_distance():
        print(self.range_a.distance_mm)
    
    def Right_distance():
        print(self.range_b.distance_mm)

    def check_forward():
        if self.range_a.distance_mm > 50:
            return False
        else:
            return True and print("stop")
    def check_right():
        if self.range_b.distance_mm > 50:
            return False
        else:
            return True and print("stop")

    

class Combined_movement(Basic_movement, Ultra_sensor_states):
    def __init__(self, Idle=True Forward=False, Right=False, Left=False):
        self.__idle = Idle
        self.__Forward = Forward
        self.__Right = Right
        self.__Left = Left

    def Idle():
        self.
    def Forward():

    def Right():

    def Left():

    def Run(self):

        if 
