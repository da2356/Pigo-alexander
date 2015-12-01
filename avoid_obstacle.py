#GOPIGO AUTOMOUS, INSTANTIATED CLASS
#http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/
from gopigo import *
import time
import sys
from collections import Counter
import math

distance_to_stop=30
#TODO: Is my camera straight?


def FindPathRight(dist):
	while dist<distance_to_stop:
		stop()
		bwd()
		time.sleep(.5)
		stop()
		right_rot()
		time.sleep(.2)
		stop()
		dist=us_dist(15)
        print "Dist:",dist,'cm'
	print "Path is now clear, I think."


def trot():
	set_left_speed(120)
	set_right_speed(165)
	fwd()

print "Press ENTER to start"
raw_input()
trot()
print "Weeeeeee"
while True:
	dist=us_dist(15)
    print "Dist:",dist,'cm'
	if dist<distance_to_stop:
		print "Something in my way. Going to look for a new path"
		stop()
		FindPathRight(dist)
	print "Let's hit the road again."
	trot()
