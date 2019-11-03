#!/usr/bin/env python

import rospy
from Tkinter import *
from geometry_msgs.msg import Twist

window = Tk()

rospy.init_node("mobot2_gui_pub_node")
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

def send():
	pub.publish(msg)
	rate.sleep()
	rospy.spin()

Button(window,fg="red",bg="green",text="AutoButton !",command=send).pack()
mainloop()


