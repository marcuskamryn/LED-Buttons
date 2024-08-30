import board
import digitalio as dio
import time

led = dio.DigitalInOut(board.GP0)
led.direction = dio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5)
