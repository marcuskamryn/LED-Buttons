import board
import digitalio as dio
import time

led_one = dio.DigitalInOut(board.D2)
led_one.direction = dio.Direction.OUTPUT

led_two = dio.DigitalInOut(board.D3)
led_two.direction = dio.Direction.OUTPUT

led_three = dio.DigitalInOut(board.D4)
led_three.direction = dio.Direction.OUTPUT

led_four = dio.DigitalInOut(board.D5)
led_four.direction = dio.Direction.OUTPUT

def on_off(name):
    name.value = True
    time.sleep(1)
    name.value = False
    time.sleep(1)

while True:
    on_off(led_one)
    on_off(led_two)
    on_off(led_three)
    on_off(led_four)
