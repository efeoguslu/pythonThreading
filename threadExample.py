from time import *
from threading import Thread


def myBox(delayT):
    while True:
        print('...........my box is open')
        sleep(delayT)
        print('...........my box is closed')
        sleep(delayT)


def myLED(delayT):
    while True:
        print('my led is on')
        sleep(delayT)
        print('my led is off')
        sleep(delayT)


delayBox = 5
delayLED = 1

boxThread = Thread(target=myBox, args=(delayBox,))
LEDThread = Thread(target=myLED, args=(delayLED,))

boxThread.daemon = True
LEDThread.daemon = True

boxThread.start()
LEDThread.start()

j = 0
while True:
    print(j)
    j = j+1
    sleep(0.1)
