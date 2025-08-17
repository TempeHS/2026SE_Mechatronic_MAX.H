import time 
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from servo import Servo
from PID_Controller import PIDControl
from PiicoDev_Unified import sleep_ms
from PiicoDev_VEML6040  import PiicoDev_VEML6040


class Basic_movement(Servo):
    def __init__(self, Right_servo, Left_servo):
        self.__Left_servo = Servo(pwm=20)
        self.__Right_servo = Servo(pwm=16)

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
    

class Check_colour(PiicoDev_VEML6040):
    def __init__(self):
        self.colourSensor = PiicoDev_VEML6040()
        self.green = 120
    
    def is_green(self):
        self.Col_det
                


class Combined_movement(Basic_movement, Ultra_sensor_states, Servo, PiicoDev_Ultrasonic):
    def __init__(self):
        self.__state = "idle"
        ultrasonic = Ultra_sensor_states(
            range_a=PiicoDev_Ultrasonic(id=[0, 0, 0, 0]),
            range_b=PiicoDev_Ultrasonic(id=[1, 0, 0, 0]) 
            )
        movement = Basic_movement(
            Right_servo=Servo(pwm=16,),
            Left_servo=Servo(pwm=20,)
            )
        self.last_forward_distance = int(ultrasonic.check_forward())
        self.last_right_distance = int(ultrasonic.check_right())

    def set_Idle(self):
        print("IDLE")
        self.movement.Stop
        self.__state = "idle"

    def set_Forward(self):
        print("FORWARD")
        self.movement.basic_forward
        self.__state = "forward"
            
    def set_Right(self):
        print("RIGHT")
        self.movement.Turn_right
        self.__state = "right"

    def set_Left(self):
        print("LEFT")
        self.movement.Turn_left
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

controller = Combined_movement()
while True:
    controller.Run()