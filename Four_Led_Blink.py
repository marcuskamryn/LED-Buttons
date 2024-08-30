import board
import digitalio as dio
import time

led_one = dio.DigitalInOut(board.GP0)
led_one.direction = dio.Direction.OUTPUT

led_two = dio.DigitalInOut(board.GP1)
led_two.direction = dio.Direction.OUTPUT

led_three = dio.DigitalInOut(board.GP2)
led_three.direction = dio.Direction.OUTPUT

led_four = dio.DigitalInOut(board.GP3)
led_four.direction = dio.Direction.OUTPUT

while True:
    led_one.value = True
    time.sleep(1)
    led_one.value = False
    time.sleep(1)

    led_two.value = True
    time.sleep(1)
    led_two.value = False
    time.sleep(1)

    led_three.value = True
    time.sleep(1)
    led_three.value = False
    time.sleep(1)

    led_four.value = True
    time.sleep(1)
    led_four.value = False
    time.sleep(1)
