import board
import digitalio as dio
import time

led = dio.DigitalInOut(board.D2)
led.direction = dio.Direction.OUTPUT

def theK():
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(.5)
    led.value = True
    time.sleep(1)
    led.value = False

def theA():
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(1)

def theM():
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep (1)

def theR():
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(.5)
    led.value = False

def theY():
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(.5)
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)

def theN():
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(.5)

while True:
    theK()
    time.sleep(1.5)
    theA()
    time.sleep(1.5)
    theM()
    time.sleep(1.5)
    theR()
    time.sleep(1.5)
    theY()
    time.sleep(1.5)
    theN()
    time.sleep(1.5)
    theM()
    time.sleep(1.5)
    theA()
    time.sleep(5)
