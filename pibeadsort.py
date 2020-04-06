import cv2
from gpiozero import Servo
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
    selectservo = initgpio(17)
    feedservo = initgpio(19)
    cam = initcam()
    runloop(cam, feedservo, selectservo)







#########

scriptpath = os.path.dirname(sys.argv[0])

def getimage(camera):
    timestamp = int(time.time())
    filename = scriptpath +'/%s.jpg' % timestamp
    camera.capture(filename)
    img = cv2.imread(filename,0) ## we need to do this directly in the future when not debugging
    return img

def findbeadcolor(image, pallet):
    # do some image processing and select most fit color
    color = None

    return color

def selectbucket(color):
    return

def nextbead():
    return 


## initialization functions
def initgpio():
    return 

def initcam():
    camera = PiCamera()
    return camera

def test():
    image = getimage(initcam())
    findbeadcolor(image, pallet)
    return 0

if __name__ == "__main__":
    test()
    #main()
