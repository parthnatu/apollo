#!/usr/bin/env python
import rospy
from time import sleep
from std_msgs.msg import String
from nanpy import ArduinoApi
from nanpy import SerialManager
from nanpy import Servo

import logging
logging.basicConfig(level=logging.DEBUG)
SERVO_PAN = 7
SERVO_TILT = 8
connection = SerialManager(device='/dev/ttyACM0')
panservo=Servo(SERVO_PAN)
tiltservo=Servo(SERVO_TILT)
panservo.write(100)
tiltservo.write(40)
sleep(1)
panservo.write(100)
tiltservo.write(40)
sleep(1)
panservo.write(100)
tiltservo.write(40)
def move_servo(data):
	global panservo
	global tiltservo
	if('move left' in data.data):
		panservo.write(panservo.read()+10)
		#tiltservo.write(tiltservo.read())
	if('move right' in data.data):
                panservo.write(panservo.read()-10)
                #tiltservo.write(tiltservo.read())


if __name__ == "__main__":
        try:
		rospy.init_node('control_servos', disable_signals=True)
        	rospy.Subscriber('/recognized_string',String,move_servo)
		rospy.spin()
	except:
		print('error')

