#!/usr/bin/env python
import speech_recognition as sr
import rospy
from speech_service.srv import *
r = sr.Recognizer()
m = sr.Microphone()

def handle_audio(x):
	print 'say.'
	with m as source: audio = r.listen(source)
	print 'recognizing...'
	try:
		value = r.recognize_google(audio)
		if str is bytes:  # this version of Python uses bytes for strings (Python 2)
			print(u"You said {}".format(value).encode("utf-8"))
			return ReturnDetectedSpeechResponse(str(value))
		else:  # this version of Python uses unicode for strings (Python 3+)
			print("You said {}".format(value))
			return ReturnDetectedSpeechResponse(str(value))
	except sr.UnknownValueError:
		return ReturnDetectedSpeech("333")
	except sr.RequestError:
		return ReturnDetectedSpeech("666")
	
def return_detected_speech():
	with m as source: r.adjust_for_ambient_noise(source)
	print("set min energy thresh to : {}".format(r.energy_threshold))
	rospy.init_node('speech_detection_node')
        s = rospy.Service('speech_detect', ReturnDetectedSpeech, handle_audio)
        print 'service ready.'
        rospy.spin()

if __name__ == "__main__":
    return_detected_speech()
