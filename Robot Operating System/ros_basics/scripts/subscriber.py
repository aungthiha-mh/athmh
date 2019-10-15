#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

def callback(msg):
	print(msg.data)
	

rospy.init_node("subscriber_node")
rospy.Subscriber("/helloworld" , String , callback)
rospy.Subscriber("/counter" , Int32 , callback)
rospy.spin()