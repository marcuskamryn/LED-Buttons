import board
from digitalio import DigitalInOut, Direction
import time

button_down = DigitalInOut(board.D2)
button_down.direction = Direction.INPUT
button_up = DigitalInOut(board.D3)
button_up.direction = Direction.INPUT

led_one = DigitalInOut(board.D4)
led_one.direction = Direction.OUTPUT

led_two = DigitalInOut(board.D5)
led_two.direction = Direction.OUTPUT

led_status = False
white = False

while True:    
    if not button_down.value:
        led_status = not led_status
        time.sleep(.20)
    
    if led_status:
        led_status = False
        led_one.value = not led_one.value
        led_two.value = led_one.value
  
  
    if not button_up.value:
        white = not white
        time.sleep(.20)
    
    if white:
        white = False
        led_one.value = not led_one.value
        led_two.value = not led_one.value
