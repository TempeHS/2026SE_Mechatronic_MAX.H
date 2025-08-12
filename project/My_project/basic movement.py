import time 
import PiicoDev_Ultrasonic
from servo import Servo
from PID_Controller import PIDControl
from PiicoDev_Unified import sleep_ms

class Basic_movement(Servo):
    def __init__(self, Right_servo, Left_servo):
        self.__Left_servo = Servo(pwm=20, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
        self.__Right_servo = Servo(pwm=16, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

    def Stop(self):
        self.__Right_servo.set_duty(1500)
        self.__Left_servo.set_duty(1500)

    def Turn_right(self):
        self.__Right_servo.set_duty(2000)
        self.__Left_servo.set_duty(1500)

    def Turn_left(self):
        self.__Right_servo.set_duty(1500)
        self.__Left_servo.set_duty(2000)

    #use with caution
    def Basic_backward(self):
        self.__Right_servo.set_duty(1000)
        self.__Left_servo.set_duty(1000)

    def basic_forward(self):
        self.__Right_servo.set_duty(2000)
        self.__Left_servo.set_duty(2000)

    def right_forward(self):
        self.__Right_servo.set_duty(1800)
        self.__Left_servo.set_duty(2000)

    def left_forward(self):
        self.__Right_servo.set_duty(2000)
        self.__Left_servo.set_duty(1800)


class Ultra_sensor_states(PiicoDev_Ultrasonic, range_a, range_b):
    def __init__(self, range_a, range_b)
        self.__range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.__range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

    def check_forward():
        return self.__range_a.distance_mm

    def check_right():
        return self.__range_b.distance_mm 
    

class Check_colour():


class Combined_movement(Basic_movement, Ultra_sensor_states, sleep_ms):
    #checkl controller for states
    def __init__(self, last_forward_distance, last_right_distance, state):
        self.state = "idle"
        self.last_forward_distance = Ultra_sensor_states.check_forward
        self.last_right_distance = Ultra_sensor_states.check_right

    def set_Idle():
        print("IDLE")
        Basic_movement.Stop
        self.state = "idle"

    def set_Forward():
        print("FORWARD")
        Basic_movement.basic_forward
        self.state = "forward"
            
    def set_Right():
        print("RIGHT")
        Basic_movement.Turn_right
        self.state = "right"

    def set_Left():
        print("LEFT")
        Basic_movement.Turn_left
        self.state = "left"

    def Run(self):
        self.state = self.set_Idle
        print("running in 3 seconds")
        sleep_ms(30)
        print("RUNNING")
        if self.last_forward_distance < 100:
            if self.last_right_distance <100:
                self.state = self.set_Left
            else:
                self.state = self.set_Right
        else:
            self.state = self.set_Forward

class debug(self, Ultra_sensor_states, Check_colour, Basic_movement)
    def __init__(self, state)
        self.state = state

    def debug_ultra_sensor():
        #print range for both sensors in sequence 
        while True
            print("forward")
            print(Ultra_sensor_states.check_forward)
            sleep_ms(5)
            print("right")
            print(Ultra_sensor_states.check_right)
            sleep_ms(5)
    
    def debug_colour():
        while True
        #check colour, red green blue in sequence while broadcasting

    def debug_movement():
        #