#!/usr/bin/env python  
import roslib
roslib.load_manifest('ros_basics')
import rospy
import tf
import turtlesim.msg

def posecallback(msg, turtlename):

  br = tf.TransformBroadcaster()
  br.sendTransform((msg.x, msg.y, 0),tf.transformations.quaternion_from_euler(0, 0, msg.theta),rospy.Time.now(),turtlename,"world")

if __name__ == '__main__':

	while not rospy.is_shutdown():

		rospy.init_node('turtle_tf_broadcaster')
		turtlename = rospy.get_param('~turtle')
		rospy.Subscriber('/%s/pose' % turtlename,turtlesim.msg.Pose,posecallback,turtlename)
		rospy.spin()
