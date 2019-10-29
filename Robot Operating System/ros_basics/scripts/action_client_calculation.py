#! /usr/bin/env python

import actionlib
import rospy

from ros_basics.msg import CalculationFeedback, CalculationResult, CalculationAction, CalculationGoal


def feedback_callback(feedback):
	print("Feedback sent ! , Goal is received > Success !")

client = actionlib.SimpleActionClient('/calculation_as', CalculationAction)

rospy.init_node('calculation_action_client')
	
client.wait_for_server()

while not rospy.is_shutdown():
	
	goal = CalculationGoal()
	goal.num1 = input('Enter a number: ')
	goal.num2 = input('Enter a number: ')
	
	client.send_goal(goal, feedback_cb = feedback_callback)
	
	client.wait_for_result()
	print '[Result] State: %d'%(client.get_state())
	print '---'