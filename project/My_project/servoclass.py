#setup servo class
import time
from machine import Pin, PWM
from servo import Servo



class Movementsubsystem:
    def __init__(self, speed, ):
        self.__speed = speed

#create diffirent movement states for wheel
    def Idle(self):
        #movement is zero
    
    def Forward(self):
        #movement is positive
    
    def Backward(self):
        #movement is negative
    
