#!/usr/bin/env python

import rospy
from ros_basics.srv import AddTwoInts,AddTwoIntsRequest

rospy.init_node("basic_client_node")
rospy.wait_for_service("/add_two_ints_server")
receive = rospy.ServiceProxy("/add_two_ints_server" , AddTwoInts)
add = AddTwoIntsRequest()

while not rospy.is_shutdown():
	add.a = int(input("Enter first number - "))
	add.b = int(input("Enter second number - "))
	print(receive(add))
