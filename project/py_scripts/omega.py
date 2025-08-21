from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from servo import Servo
from PiicoDev_Unified import sleep_ms
from PiicoDev_VEML6040  import PiicoDev_VEML6040
from machine import PWM, Pin

#(Servo)
class Basic_movement:
    def __init__(self, Left_servo, Right_servo):
        self.__Left_servo = Servo(Left_servo)
        self.__Right_servo = Servo(Right_servo)

    def Stop(self):
        self.__Right_servo.set_duty(1500)
        self.__Left_servo.set_duty(1500)

    def Turn_right(self):
        self.__Right_servo.set_duty(1500)
        self.__Left_servo.set_duty(2000)

    def Turn_left(self):
        self.__Right_servo.set_duty(1000)
        self.__Left_servo.set_duty(1500)

    #use with caution
    def Basic_backward(self):
        self.__Right_servo.set_duty(2000)
        self.__Left_servo.set_duty()

    def basic_forward(self):
        self.__Right_servo.set_duty(1000)
        self.__Left_servo.set_duty(2000)

    # def right_forward(self):
    #     self.__Right_servo.set_duty(1800)
    #     self.__Left_servo.set_duty(2000)

    # def left_forward(self):
    #     self.__Right_servo.set_duty(2000)
    #     self.__Left_servo.set_duty(1800)

#(PiicoDev_Ultrasonic)
class Ultra_sensor_states:
    def __init__(self, range_a, range_b):
        self.__range_a = range_a
        self.__range_b = range_b

    def check_forward(self):
        return int(self.__range_a.distance_mm)

    def check_right(self):
        return int(self.__range_b.distance_mm)
    
#(PiicoDev_VEML6040)
class Check_colour:
    def __init__(self, colourSensor):
        self.colourSensor = colourSensor
        self.data = self.colourSensor.readHSV()
        self.hue = self.data['hue']
    def Green(self):
        if 0 < self.hue < 1750:
            print("oh no a person")
            return True
        return False


#(Basic_movement, Ultra_sensor_states, Servo, PiicoDev_Ultrasonic)
class Combined_movement:
    def __init__(self,):
        self.__state = "idle"
        self.ultrasonic = Ultra_sensor_states(
            range_a=PiicoDev_Ultrasonic(id=[0, 0, 0, 0]),
            range_b=PiicoDev_Ultrasonic(id=[1, 0, 0, 0]) 
            )
        self.movement = Basic_movement(PWM(Pin(16)), PWM(Pin(20)))
        self.last_forward_distance = int(self.ultrasonic.check_right())
        self.last_right_distance = int(self.ultrasonic.check_forward())
        self.coloursensor = Check_colour(PiicoDev_VEML6040())

    def set_dead(self):
        print("oh no a dead person")
        self.movement.Stop()
        sleep_ms(5000)
        self.__state = "dead"

    def set_Idle(self):
        print("IDLE")
        self.movement.Stop()
        self.__state = "idle"

    def set_Forward(self):
        print("FORWARD")
        self.movement.basic_forward()
        self.__state = "forward"
            
    def set_Right(self):
        print("RIGHT")
        self.movement.Turn_right()
        self.__state = "right"

    def set_Left(self):
        print("LEFT")
        self.movement.Turn_left()
        self.__state = "left"

    def Run(self):
        print("RUNNING")
        forward_distance = self.ultrasonic.check_forward()
        right_distance = self.ultrasonic.check_right()


        if self.__state == "idle":
            self.set_Idle()
            sleep_ms(2000)
            self.set_Forward()

        elif self.__state == "forward":
            self.set_Forward()

            if forward_distance < 100 and right_distance < 100:
                self.set_Right()
                # sleep_ms(2000)

            elif right_distance < 100:
                self.set_Left()
                # sleep_ms(2000)

            elif self.coloursensor.Green():
                self.set_dead()
                sleep_ms(2000)
                self.set_Forward() 

            else:
                self.set_Forward()
        else:
            self.set_Idle()
            print("broken, one sec")


# class debug(Ultra_sensor_states, Check_colour, Basic_movement):
#     def __init__(self, state):
#         self.state = state
        

    # def debug_ultra_sensor(self):
    #     sensor = Ultra_sensor_states(
    #     range_a=PiicoDev_Ultrasonic(id=[0, 0, 0, 0]),
    #     range_b=PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
    #     )
    #     while True:
    #         print("forward:", sensor.check_forward())
    #         sleep_ms(5)
    #         print("right:", sensor.check_right())
    #         sleep_ms(5)
    
    # def debug_colour(self):
    #     while True:
    #         #check colour, red green blue in sequence while broadcasting
    #         ...

    # def debug_movement(self):
    #
    #     ...

controller = Combined_movement()
while True:
    controller.Run()