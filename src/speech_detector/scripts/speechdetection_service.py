#!/usr/bin/env python
import speech_recognition as sr
import rospy
import snowboydecoder
from time import sleep
r = sr.Recognizer()
MODEL = "resources/computer.pmdl"
detector = snowboydecoder.HotwordDetector(MODEL, sensitivity=0.5)
def handle_audio():
	global detector
	detector.terminate()
	m = sr.Microphone()
	print 'say'
	with m as source: audio = r.listen(source)
	print 'recognizing...'
	try:
		value = r.recognize_google(audio,language='en-GB')
		if str is bytes:  # this version of Python uses bytes for strings (Python 2)
			#print(u"You said {}".format(value).encode("utf-8"))
			print(str(value))
		else:  # this version of Python uses unicode for strings (Python 3+)
			#print("You said {}".format(value))
			print(str(value))
	except sr.UnknownValueError:
		print("unknown_text")
	except sr.RequestError:
		print("connection error")
	del m
	return

if __name__ == "__main__":
	rospy.init_node('speech_node', disable_signals=True)
	try:
		while(True):
			detector.start(detected_callback=handle_audio,sleep_time=0.03)
			#sleep(10)
	except KeyboardInterrupt:
		detector.terminate()
		print 'ended'
