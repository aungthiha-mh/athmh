#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("mobot2_auto_pub_node")
pub = rospy.Publisher("/cmd_vel" , Twist , queue_size = 1)

r = 1
velocity = 0.2
distance = 100
time = distance/velocity
ticks = r*time

rate = rospy.Rate(r)

msg = Twist()

msg.linear.x = velocity
msg.angular.z = velocity

while not rospy.is_shutdown():

	pub.publish(msg)

	rospy.loginfo(rospy.get_time())
	rospy.loginfo(ticks)
	rate.sleep()
	rospy.spin()


