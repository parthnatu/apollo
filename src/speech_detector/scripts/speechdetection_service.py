#!/usr/bin/env python
import speech_recognition as sr
import rospy
import time
import snowboydecoder
import sox
import rospkg
from time import sleep
from std_msgs.msg import Bool
import os
r = sr.Recognizer()
rospack = rospkg.RosPack()
MODEL = rospack.get_path('speech_detector')+"/scripts/resources/models/snowboy.umdl"
detector = snowboydecoder.HotwordDetector(MODEL, sensitivity=0.5)
tfm = sox.Transformer()
tfm.convert(samplerate=16000,bitdepth=16)
pub = rospy.Publisher('google_assistant',Bool,queue_size=10)
ready = True
def ready_hotword(data):
	global ready
	ready = data.data
def handle_audio():
	
	global detector
	global pub
	detector.terminate()
	m = sr.Microphone()
	print 'say'
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.01, 300))
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.01, 600))
	#os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.01, 550))
	#os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.01, 600))
	with m as source: audio = r.listen(source)
	start = time.time()
	with open('file.wav','wb') as f:
		f.write(audio.get_wav_data(convert_rate=160000))
	tfm.build('file.wav',rospack.get_path('voice_file')+'/user_query.wav')
	#sleep(1)
	pub.publish(True)
	#alexa.ask('file_.wav',save_to = './test.mp3)
	print 'recognizing...'
	try:
		value = r.recognize_google(audio,language='en-GB')
		if str is bytes:
			print(str(value))
	except sr.UnknownValueError:
		print("unknown_text")
	except sr.RequestError:
		print("connection error")
	del m
	return

if __name__ == "__main__":
	rospy.init_node('speech_node', disable_signals=True)
	rospy.Subscriber('ready_hotword',Bool,ready_hotword)
	try:
		while(True):
			if(ready):
				detector.start(detected_callback=handle_audio,sleep_time=0.03)
	except KeyboardInterrupt:
		detector.terminate()
		print 'ended'
