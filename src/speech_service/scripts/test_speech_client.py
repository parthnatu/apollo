#!/usr/bin/env python
import rospy
from speech_service.srv import *
def detect_speech():
	rospy.wait_for_service('speech_detect')
	try:
		speech_det = rospy.ServiceProxy('speech_detect',ReturnDetectedSpeech)
		response = speech_det()
		return response.text
	except rospy.ServiceException, e:
		print 'service call failed.'
if __name__ == "__main__":
	print(detect_speech())
