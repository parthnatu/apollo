#!/usr/bin/env python
import pyaudio
import wave
import speech_recognition as sr
import rospy
import time
import snowboydecoder
import sox
import rospkg
from time import sleep
from std_msgs.msg import Bool
from std_msgs.msg import String
import os
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
panservo.write(40)
tiltservo.write(55)
sleep(1)
panservo.write(40)
tiltservo.write(55)
sleep(1)
panservo.write(40)
tiltservo.write(55)

r = sr.Recognizer()
rospack = rospkg.RosPack()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = rospack.get_path('voice_file')+'/user_query.wav'
MODEL = rospack.get_path('speech_detector')+"/scripts/resources/models/snowboy.umdl"
detector = snowboydecoder.HotwordDetector(MODEL, sensitivity=0.8)
#tfm = sox.Transformer()
#tfm.convert(samplerate=16000,bitdepth=16)
pubstr = rospy.Publisher('recognized_string',String,queue_size=10)
pub = rospy.Publisher('google_assistant',Bool,queue_size=10)
ready = True
def move_servo(data):
        global panservo
        global tiltservo
	global pub
        if('move left' in data):
                panservo.write(panservo.read()+35)
                tiltservo.write(tiltservo.read())
        if('move right' in data):
                panservo.write(panservo.read()-35)
                tiltservo.write(tiltservo.read())
def ready_hotword(data):
	global ready
	ready = data.data
def handle_audio():
	pubstr.publish(str("SPEAK, HUMAN."))
	global ready
	global detector
	global pub
	ready = False
	detector.terminate()
	print 'say'
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.01, 300))
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.01, 600))
	save_audio()
	#os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.01, 550))
	#os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.01, 600))
	with  sr.WavFile(WAVE_OUTPUT_FILENAME) as source: audio = r.listen(source)
	#start = time.time()
	#with open('file.wav','wb') as f:
	#	f.write(audio.get_wav_data(convert_rate=160000))
	#tfm.build('file.wav',rospack.get_path('voice_file')+'/user_query.wav')
	#sleep(1)
	#pub.publish(True)
	#alexa.ask('file_.wav',save_to = './test.mp3)
	print 'recognizing...'
	try:
		value = r.recognize_google(audio,language='en-GB')
		pubstr.publish(str(value))
		if "move left" in value or "move right" in value:
			print(str(value))
			#pubstr.publish(str(value))
			move_servo(value)
			pub.publish(False)
			ready = True
			return
		if str is bytes:
			print(str(value))
	except sr.UnknownValueError:
		print("unknown_text")
	except sr.RequestError:
		print("connection error")
	pub.publish(True)
	#sleep(1)
	return

def save_audio():
	audio = pyaudio.PyAudio()

	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
	print "recording..."
	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    		data = stream.read(CHUNK)
    		frames.append(data)
	print "finished recording"


	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()

	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()

if __name__ == "__main__":
	rospy.init_node('speech_node', disable_signals=True)
	rospy.Subscriber('ready_hotword',Bool,ready_hotword)
	#rospy.Subscriber('/recognized_string',String,move_servo)
	try:
		while(True):
			if(ready):
				detector.start(detected_callback=handle_audio,sleep_time=0.03)
	except KeyboardInterrupt:
		detector.terminate()
		print 'ended'
