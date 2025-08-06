#setup servo class
import time
from machine import Pin, PWM
from servo import Servo



class Movementsubsystem(Servo):
    def __init__(self, Forward, ):
        self.__speed = 

#create diffirent movement states for wheel
    def Idle(self):
        self.set_duty = 1500
        #movement is zero
    
    def Forward(self):
        self.set_duty = 1000
        #movement is positive
    
    def Backward(self):
        self.set_duty = 2000
        #movement is negative
    
    def Right_move(self):
        #take movement both wheel to go right
    
    def Left_move(self):
        #take movement of both wheel to go left