#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('google_assistant', Bool, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
