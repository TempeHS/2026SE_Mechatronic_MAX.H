from omega import Basic_movement
from servo import Servo
from PiicoDev_Unified import sleep_ms

left_servo = Servo(16)
right_servo = Servo(20)

print(f"starting unittest \n moving forward for 3 seconds")
Basic_movement.basic_forward()
sleep_ms(30)
print("moving backward for 3 seconds")
Basic_movement.Basic_backward()
sleep_ms(30)
print("stopping for 3 seconds")
Basic_movement.Stop
sleep_ms(30)
print("turning right for 3 seconds")
Basic_movement.Turn_right()
sleep_ms(30)
print("turning left for 3 seconds")
Basic_movement.Turn_left
sleep_ms(30)
print("ending unittest")