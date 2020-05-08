import cv2
from gpiozero import Servo , LED
from picamera import PiCamera
import time 
import datetime
import sys
import os


#define names for the hex values and tolerance in percent (of 255) 
pallet = {
    "red": { "value":0xff0000, "tolerance":(0.1, 0.1, 0.1)},
    "green": { "value":0x00ff00, "tolerance":(0.1, 0.1, 0.1)},
    "blue": { "value":0x0000ff, "tolerance":(0.1, 0.1, 0.1)},
}

binpositions = {
    "red": 10,
    "green": 50,
    "blue": 90,
}

feedservomid = -0.025

#servo = Servo(17)

#while True:
#    servo.min()
#    sleep(2)
#    servo.mid()
#    sleep(2)
#    servo.max()
#    sleep(2)



def runloop(cam, feedservo, selectservo):
    while 1:
        image = getimage(cam)
        color = findbeadcolor(image, pallet)
        selectbucket(color, selectservo, binpositions)
        nextbead(feedservo)

def main():
    selectservo = initservo(17)
    feedservo = initservo(19)
    cam = initcam()
    runloop(cam, feedservo, selectservo)







#########

scriptpath = os.path.dirname(sys.argv[0])

def getimage(camera):
    timestamp = int(time.time())
    filename = scriptpath +'/%s.jpg' % timestamp
    camera.capture(filename)
    ## we need to do this directly in the 
    img = cv2.imread(filename,0) 
    #future when not debugging
    return img

def findbeadcolor(image, pallet):
    # do some image processing and select most fit color
    color = None




    return color

def selectbucket(color):
    return

def nextbead(blocker,releaser):
    releaser.openclose()
    blocker.openclose()
    return 


## initialization functions
def initservo(pin,initial_value=None):
    servo = Servo(
        pin, 
        initial_value=initial_value, 
        min_pulse_width=0.49/1000,
        max_pulse_width=2.3/1000.
    )
    return servo

class Barrier(Servo):
    def __init__(self, pin,closevalue, openvalue=0):
        self.openvalue = openvalue
        self.closevalue = closevalue
        super(Barrier, self).__init__(
            pin, 
            initial_value=closevalue, 
            min_pulse_width=0.49/1000,
            max_pulse_width=2.3/1000.
        )
    def open(self): 
        self.value = self.openvalue
        time.sleep(0.2)
    def close(self):
        self.value = self.closevalue
        time.sleep(0.2)
        self.value = None
    def openclose(self):
        self.open()
        self.close()

def initcam():
    camera = PiCamera()
    return camera

def test():
    #image = getimage(initcam())
    #findbeadcolor(image, pallet)
    #selectservo = initservo(4)
    #feedservo = initservo(17)
    #feedservo.value = feedservomid

    blocker = Barrier(23,-0.8, -0.65) # initservo(23, -0.8)
    blocker.close()
    releaser = Barrier(24, 0.75 , 0.55) # initservo(24, 0.75)
    releaser.close()

    while True:
        #selectservo.min()
        nextbead(blocker, releaser)

        time.sleep(0.7)
        #selectservo.mid()
        #time.sleep(1)
        #selectservo.max()
        #time.sleep(0.7)


    return 0

if __name__ == "__main__":
    test()
    #main()
