#!/usr/bin/env python

import rospy
from ros_basics.srv import AddTwoInts,AddTwoIntsResponse

def callback(request):
	answer = request.a + request.b
	print "Returning [%s + %s = %s]" % (request.a, request.b, (answer))
	return AddTwoIntsResponse(answer)

rospy.init_node("basic_server_node")
rospy.Service("/add_two_ints_server" , AddTwoInts , callback)
print("Server is ready,you can add two numbers")
rospy.spin()