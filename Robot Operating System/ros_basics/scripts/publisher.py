#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
rospy.init_node("publisher_node")
pub = rospy.Publisher("/helloworld" , String , queue_size = 1)
pub1 = rospy.Publisher("/counter" , Int32 , queue_size = 1)
rate = rospy.Rate(2)

hello = String()
count = Int32()
hello.data = "Hello World"
count.data = 0
while not rospy.is_shutdown():
	one = pub1.publish(count)
	two = pub.publish(hello)
	count.data +=1
	if count.data == 100:
		break
	rate.sleep()
print("The number is finished")