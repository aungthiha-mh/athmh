#! /usr/bin/env python

import actionlib
import rospy

from ros_basics.msg import *

class DemoClass(object):

	_feedback = DemoFeedback()
	_result   = DemoResult()

	_feedback.current_number = 0

	def __init__(self):
		self._as = actionlib.SimpleActionServer("demo_as", DemoAction, self.goal_callback, False)
		self._as.start()

	def goal_callback(self, goal):
		r = rospy.Rate(1)
		success = True

		progress = goal.count
		for i in range(0, progress):

			if self._as.is_preempt_requested():
				rospy.loginfo("The goal has been cancelled")
				self._as.set_preempted()
				success = False
				break

			self._feedback.current_number += 1
			self._as.publish_feedback(self._feedback)

			r.sleep()

		if success:
			self._result.final_count = self._feedback.current_number
			rospy.loginfo("Succeeded! Final goal, count = %s" % self._result.final_count)
			self._as.set_succeeded(self._result)

if __name__ == '__main__':
	rospy.init_node("demo")
	DemoClass()
	rospy.spin()