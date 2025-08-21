from omega import Ultra_sensor_states
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
import time
PiicoDev_Unified import sleep_ms

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

print("starting unittest \n check ranges for 5 seconds")

timer = time.time() + 3

while time.time() < timer:
    print(f"forward distance: {range_a}\nright distance: {range_b}")
    sleep_ms(2)

print("finished unittest")