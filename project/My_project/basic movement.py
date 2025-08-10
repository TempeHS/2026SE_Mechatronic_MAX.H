import time 
import PiicoDev_Ultrasonic
from servo import Servo
from PID_Controller import PIDControl
from PiicoDev_Unified import sleep_ms

class Basic_movement(Servo):
    def __init__(self, Right_servo, Left_servo):
        self.Left_servo = Servo(pwm=servo_pwm, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
        self.Right_servo = Servo(pwm=servo_pwm, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

    def Stop(self):
        self.Right_servo.set_duty(1500)
        self.Left_servo.set_duty(1500)

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

class Ultra_sensor_states(PiicoDev_Ultrasonic, Basic_movement):
    def __init__(self, range_a, range_b)
        self.range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

    def check_forward():
        return self.range_a.distance_mm

    def check_right():
        return self.range_b.distance_mm 

    

class Combined_movement(Basic_movement, Ultra_sensor_states):
    #checkl controller for states
    def __init__(self, ):
        self.state = "IDLE"
    #check controller
    def set_state(self):

    def Idle():
        print("IDLE")
        Basic_movement.Stop
    def Forward():
        last_forward_distance = Ultra_sensor_states.check_forward
        last_right_distance = Ultra_sensor_states.check_right
        print("FORWARD")
        sleep_ms(5)
        if Ultra_sensor_states.check_forward < 20:
            if Ultra_sensor_states.check_right <20:
        else:
            self.state = self.set_state_forward

    def Right():
        print("RIGHT")
    def Left():
        print("LEFT")

    def Run(self):
        print("RUNNING")
        if 
