import time 
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
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


class Ultra_sensor_states(PiicoDev_Ultrasonic):
    def __init__(self, range_a, range_b):
        self.__range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.__range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

    def check_forward(self):
        return int(self.__range_a.distance_mm)

    def check_right(self):
        return int(self.__range_b.distance_mm)
    

class Check_colour():
    def __init__(self, ):
        ...


class Combined_movement(Basic_movement, Ultra_sensor_states, sleep_ms):
    #checkl controller for states
    def __init__(self, last_forward_distance, last_right_distance, state):
        self.__state = "idle"
        self.last_forward_distance = int(Ultra_sensor_states.check_forward(self))
        self.last_right_distance = int(Ultra_sensor_states.check_right(self))

    def set_Idle(self):
        print("IDLE")
        Basic_movement.Stop
        self.__state = "idle"

    def set_Forward(self):
        print("FORWARD")
        Basic_movement.basic_forward
        self.__state = "forward"
            
    def set_Right(self):
        print("RIGHT")
        Basic_movement.Turn_right
        self.__state = "right"

    def set_Left(self):
        print("LEFT")
        Basic_movement.Turn_left
        self.__state = "left"

    def Run(self):
        print("RUNNING")
        if self.last_forward_distance < 100:
            if self.last_right_distance < 100:
                self.set_Left()
            else:
                self.set_Right()
        else:
            self.set_Forward()

class debug(Ultra_sensor_states, Check_colour, Basic_movement):
    def __init__(self, state):
        self.state = state
        

    def debug_ultra_sensor(self):
        #print range for both sensors in sequence 
        while True:
            print("forward")
            print(Ultra_sensor_states.check_forward)
            sleep_ms(5)
            print("right")
            print(Ultra_sensor_states.check_right)
            sleep_ms(5)
    
    def debug_colour(self):
        while True:
            #check colour, red green blue in sequence while broadcasting
            ...

    def debug_movement(self):
        #
        ...

while True:
    Combined_movement.Run(self)