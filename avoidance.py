from gopigo import *
import time
STOP_DIST = 50
class Pigo:
    vision = [None] * 180
    opt1, opt2 = 0, 0
    wentleftlast = True
    status = {"ismoving": False, "servo": 90, "leftspeed": 175, "rightspeed": 175, 'dist': 100}

    def __init__(self):
        print "I'm such a Pigo.  beep beep."
        self.checkDist()

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




    def stop(self):
        self.status["isMoving"] = False
        print "Oh boy"
        for x in range(3):
            stop()
    def allStop(self):
        print "Stopping"
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

    def servoSweep(self):
        print "Sweeping now"
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.1)
            self.vision[ang] = us_dist(15)
        servo(90)

    def checkTwenty(self):
        self.opt1 = None
        self.opt2 = None
        for ang in range(20, 160, 2):
            counter = 0
            if self.vision[ang] > 50:
                counter += 1
            else:
                counter = 0
            if counter == 10:
                if self.opt1:
                    self.opt2 = ang - 10
                else:
                    self.opt1 = ang - 10
                print ang
                return ang

    def turnTo(self):
        bigturn = .26
        midturn = .2
        smturn = .12
        sec = .1
        print "Our first option is:" + str(self.opt1)
        if self.opt1 == 0:
            self.turnAway()
        turnchoice = self.opt1
        if self.opt2 != 0 and not self.wentleftlast:
            turnchoice = self.opt2
        if turnchoice <= 90:
            self.wentleftlast = True
        else:
            self.wentleftlast = False
        print "Turnchoice is set to: " + str(turnchoice)
        if 20 <= turnchoice < 40:
            sec = .26
        elif 40 <= turnchoice < 60:
            sec = .2
        elif 60 <= turnchoice < 80:
            sec = .12
        elif 80 <= turnchoice < 100:
            sec = 0
        elif 100 <= turnchoice < 120:
            sec = .12
        elif 120 <= turnchoice < 140:
            sec = .2
        elif 140 <= turnchoice < 160:
            sec = .26
        if turnchoice < 90:
            left()
            time.sleep(sec)
            self.stop()
        else:
            right()
            time.sleep(sec)
            self.stop()
    def turnAway(self):
        bwd()
        time.sleep(1.5)
        self.stop()

tina = Pigo()
while True:
    if tina.keepGoing():
        tina.safeDrive()
    else:
        tina.servoSweep()
        tina.checkTwenty()
        tina.turnTo()


tina.stop()
