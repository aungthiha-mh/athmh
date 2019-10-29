#! /usr/bin/env python

import actionlib
import rospy

from ros_basics.msg import *

class CalculationClass(object):

	_feedback = CalculationFeedback()
	_result   = CalculationResult()

	_feedback.situation = 0

	def __init__(self):
		self._as = actionlib.SimpleActionServer("/calculation_as", CalculationAction, self.goal_callback, False)
		self._as.start()

	def goal_callback(self, goal):
		r = rospy.Rate(1)
		success = True

		progress1 = goal.num1
		progress2 = goal.num2

		if self._as.is_preempt_requested():
			rospy.loginfo("The goal has been cancelled")
			self._as.set_preempted()
			success = False

		self._as.publish_feedback(self._feedback)

		r.sleep()

		if success:
			self._result.answer = progress1 + progress2
			rospy.loginfo("Succeeded! Final goal, Sum is %s" % self._result.answer)
			self._as.set_succeeded(self._result)

if __name__ == '__main__':
	rospy.init_node("calculation_action_server")
	CalculationClass()
	rospy.spin()