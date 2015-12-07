from gopigo import *
import time
STOP_DIST = 50
class Pigo:
    status = {"ismoving": False, "servo": 90, "leftspeed": 175, "rightspeed": 175, 'dist': 100}

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

    def turnAway(self):
        enable_encoders()
        enc_tgt(1, 0, 18)
        right_rot()
        fwd()
        time.sleep(1)
        self.stop()
        enable_encoders()
        enc_tgt(1, 0, 18)
        right_rot()
    def test(self):
        right_rot()
        time.sleep(.1)
        self.stop()
self.test()