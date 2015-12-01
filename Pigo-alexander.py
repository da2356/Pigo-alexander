#GOPIGO AUTOMOUS, INSTANTIATED CLASS
#http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/
from gopigo import *
import time
STOP_DIST = 50
class Pigo:

    status = {"ismoving": False, "servo": 90, "leftspeed": 175, "rightspeed": 175, 'dist': 100}

    def __init__(self):
        print "I'm such a Pigo.  beep beep."
        self.checkDist()
    def stop(self):
        self.status["isMoving"] = False
        print "Oh boy"
        for x in range(3):
            stop()
    def fwd(self):
        self.isMoving = True
        print "Let's do this."
        for x in range(3):
            fwd()
    def servo(self, pos):
        self.status['servo'] = pos
        servo(pos)

    def avoidLook(self):
        self.stop()
        while True:
            dist = us_dist(15)
            if dist <= 15:
                self.servoChange()

    def servoChange(self):
        enable_servo()
        if self.status['servo'] == 90:
            self.servo(140)
        elif self.status['servo'] > 90:
            self.servo(40)
        elif self.status['servo'] < 90:
            self.servo(140)
        disable_servo()


    def bwd(self):
        self.isMoving = True
        print "Back it up."
        for x in range(3):
            bwd()
    #check if conditions are safe to continue operating
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "Obstacle detected.  Stopping."
            return False
        elif volt() > 14 or volt() < 6:
            print "Unsafe voltage detected: " + str(volt())
            return False
        else:
            return True
    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "I see something " + str(self.status['dist']) + "mm away."
        if not self.keepGoing():
            print "EMERGENCY STOP FROM THE CHECK DISTANCE METHOD!!!"
            self.stop()
    def circleRight(self):
        self.status['ismoving'] = True
        print "Lets go around"
        for x in range(3):
            right()
        time.sleep(2.5)
        self.stop()
        set_left_speed(75)
        set_right_speed(215)
        for x in range(3):
            fwd()
        time.sleep(1.5)
        self.stop()
        set_left_speed(200)
        set_right_speed(200)

    def circleLeft(self):
        self.status['ismoving'] = True
        print "We're going around the other way"
        for x in range(3):
            left()
        time.sleep(2.5)
        self.stop()
        set_left_speed(215)
        set_right_speed(75)
        for x in range(3):
            fwd()
        time.sleep(1.5)
        self.stop()
        set_left_speed(200)
        set_right_speed(200)
    def servoScan(self):
        print "Looking for threats"
        for x in range(20,160,5):
            servo(x)
            time.sleep(.3)
    def shuffle(self):
        print "Get down and shuffle."
        fwd()
        time.sleep(1)
        self.stop()
        time.sleep(.1)
        bwd()
        time.sleep(1)
        self.stop()
        time.sleep(.1)
        left()
        time.sleep(1)
        self.stop()
        time.sleep(.1)
        right()
        time.sleep(1)
        self.stop()
        time.sleep(.1)
        print "Lets shake things up."
    def servoShake(self):
        for x in range(2):
            servo(20)
            time.sleep(.1)
            servo(160)
            time.sleep(.1)
            servo(90)
            time.sleep(.1)
        for x in range(2):
            servo(90)
            time.sleep(.1)
            servo(160)
            time.sleep(.1)
            servo(20)
            time.sleep(.1)
        print "Stop looking at me!!!"

    def blink(self):
        for x in range(5):
            led_on(1)

            led_on(0)
            time.sleep(.1)
            led_off(1)
            led_off(0)
        print "The big finish!"
    def safeDrive(self):
        self.fwd()
        while self.keepGoing():
            self.checkDist()
        self.stop()
    vision = []
    def servoSweep(self):
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.1)
            vison[ang] = us_dist(15)
    def checkTwenty(self):
        for ang in range(20, 160, 2):
            counter = 0
            if vision[ang] > 50:
                counter += 1
            else:
                counter = 0
            if counter == 10:
                return ang
    def turnTo(self):
        enable_encoders()
        enc_tgt(1, 0, )

    def turnAway(self):




    def dance(self):
        print "I just want to DANCE!"
        if self.keepGoing():
            self.circleRight()
            self.circleLeft()
            self.servoScan()
            self.shuffle()
            self.servoShake()
            self.blink()



tina = Pigo()

tina.stop()

