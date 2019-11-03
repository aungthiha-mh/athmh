#!/usr/bin/env python  
import roslib
roslib.load_manifest('ros_basics')
import rospy
import tf
import tf2_msgs.msg

def TFcallback(msg, mobotname):

  br = tf.TransformBroadcaster()
  br.sendTransform((msg.x, msg.y, 0),tf.transformations.quaternion_from_euler(0, 0, msg.z),rospy.Time.now(),mobotname,"world")

if __name__ == '__main__':

	while not rospy.is_shutdown():

		rospy.init_node('mobot_tf_broadcaster_node')
		mobotname = rospy.get_param('~mobot')
		rospy.Subscriber('/%s/TFMessage' % mobotname,tf2_msgs.msg.TFMessage,TFcallback,mobotname)
		rospy.spin()
