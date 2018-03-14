#!/usr/bin/env python
from helper.includes.pushtotalk import *
import rospkg
import rospy
from time import sleep
from std_msgs.msg import Bool
from subprocess import call
ASSISTANT_API_ENDPOINT = 'embeddedassistant.googleapis.com'
cred_path=os.path.join(click.get_app_dir('google-oauthlib-tool'),'credentials.json')
pub = rospy.Publisher('ready_hotword',Bool,queue_size=10)
def g_assist(data,args):
    """audio_sink =  audio_helpers.WaveSink(
              open(args[13],'wb'),
              sample_rate=args[6],
              sample_width=args[7],
      )"""
    pub.publish(False)
    #sleep(1)
    audio_sink =  audio_helpers.SoundDeviceStream(
              sample_rate=args[6],
              sample_width=args[7],
              block_size=args[10],
              flush_size=args[11]
      )
    audio_source = audio_helpers.WaveSource(
              open(args[12], 'rb'),
              sample_rate=args[6],
              sample_width=args[7]
      )
    conversation_stream = audio_helpers.ConversationStream(
          source=audio_source,
          sink=audio_sink,
          iter_size=args[8],
          sample_width=args[9],
      )
    with SampleAssistant(args[0],args[1],args[2],conversation_stream,args[3],args[4],args[5]) as assistant:
      if(data.data):
        assistant.assist()
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.02, 600))
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.02, 300))
        pub.publish(True)
        return


def main(api_endpoint=ASSISTANT_API_ENDPOINT, credentials=cred_path,
         device_model_id='testmodel_pi', device_id='testdevice_pi', device_config='device_config.json', lang='en-US', verbose=False,
         input_audio_file=rospkg.RosPack().get_path('voice_file')+'/user_query.wav',output_audio_file =rospkg.RosPack().get_path('voice_file')+'/output.wav',
         audio_sample_rate=16000, audio_sample_width=audio_helpers.DEFAULT_AUDIO_SAMPLE_WIDTH,
         audio_iter_size=audio_helpers.DEFAULT_AUDIO_ITER_SIZE, audio_block_size=audio_helpers.DEFAULT_AUDIO_DEVICE_BLOCK_SIZE,
         audio_flush_size=audio_helpers.DEFAULT_AUDIO_DEVICE_FLUSH_SIZE,grpc_deadline=60*3+5, once=True):
    if(True):
      rospy.init_node('google_assistant')
      print('init_node')
      # Load OAuth 2.0 credentials.
      try:
          with open(credentials, 'r') as f:
              credentials = google.oauth2.credentials.Credentials(token=None,
                                                                  **json.load(f))
              http_request = google.auth.transport.requests.Request()
              credentials.refresh(http_request)
      except Exception as e:
          logging.error('Error loading credentials: %s', e)
          logging.error('Run google-oauthlib-tool to initialize '
                        'new OAuth 2.0 credentials.')
          sys.exit(-1)

      # Create an authorized gRPC channel.
      grpc_channel = google.auth.transport.grpc.secure_authorized_channel(
          credentials, http_request, api_endpoint)
      logging.info('Connecting to %s', api_endpoint)

      # Configure audio source and sink.
      device_handler = device_helpers.DeviceRequestHandler(device_id)
      print('after dev handle')
          # If file arguments are supplied:
          # exit after the first turn of the conversation.
      rospy.Subscriber('google_assistant',Bool,g_assist,(lang, device_model_id, device_id,grpc_channel, grpc_deadline,
                                                         device_handler,audio_sample_rate,audio_sample_width,audio_iter_size,
                                                         audio_sample_width,audio_block_size,audio_flush_size,input_audio_file,output_audio_file))
      rospy.spin()

if __name__=="__main__":
     main()

