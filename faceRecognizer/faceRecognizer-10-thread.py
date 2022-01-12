from threading import Thread
import time

def BigBox(color, length):
    while True:
        print(color, 'Big box is open of length ', length)
        time.sleep(5)
        print(color, 'Big box is closed of length ', length)
        time.sleep(5)

def SmallBox(color, length ):
    while True:
        print(color, 'Small box is open of length ', length)
        time.sleep(1)
        print(color, 'Small box is closed of length ', length)
        time.sleep(1)

bigBoxThread = Thread(target = BigBox, args=('red', 4)) # mind the comma if you pass only 1 parameter
smallBoxThread = Thread(target = SmallBox, args=('blue', 5))

bigBoxThread.daemon = True
smallBoxThread.daemon = True
bigBoxThread.start()
smallBoxThread.start()

while True:
    pass
