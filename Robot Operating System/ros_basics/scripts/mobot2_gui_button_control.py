#!/usr/bin/env python

import rospy
from Tkinter import *
from geometry_msgs.msg import Twist

window = Tk()

rospy.init_node("mobot2_gui_node")
pub = rospy.Publisher("/cmd_vel" , Twist , queue_size = 1)

#rate = rospy.Rate(50)

msg = Twist()

def forward():
	msg.linear.x = 1.0
	msg.linear.y = 1.0
	msg.linear.z = 1.0
	pub.publish(msg)
	#rate.sleep()


def backward():
	msg.linear.x = -1.0
	msg.linear.y = -1.0
	msg.linear.z = -1.0
	pub.publish(msg)
	#rate.sleep()

def left():
	msg.angular.z = 1.0
	pub.publish(msg)
	#rate.sleep()

def right():
	msg.angular.z = -1.0
	pub.publish(msg)
	#rate.sleep()

def stop():
	msg.linear.x = 0.0
  	msg.angular.z = 0.0
	pub.publish(msg)
	#rate.sleep()

Button(window,fg="red",bg="green",text="Forward !",command=forward).pack()
Button(window,fg="red",bg="green",text="Backward !",command=backward).pack()
Button(window,fg="red",bg="green",text="Left !",command=left).pack()
Button(window,fg="red",bg="green",text="Right !",command=right).pack()
Button(window,fg="red",bg="green",text="Stop !",command=stop).pack()

mainloop()


