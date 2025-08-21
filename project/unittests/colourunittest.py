from omega import Check_colour
from PiicoDev_VEMLO6040 import PiicoDev_VEML6040

print("hold over green")
coloursensor = Check_colour(PiicoDev_VEML6040())

while True:
    if coloursensor.Green():
        print("green")
    else:
        print("not green")