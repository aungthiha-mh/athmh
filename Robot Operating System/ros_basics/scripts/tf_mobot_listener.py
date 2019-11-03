#!/usr/bin/env python  
import roslib
roslib.load_manifest('ros_basics')
import rospy
import math
import tf
import geometry_msgs.msg
import gazebo_msgs.srv

if __name__ == '__main__':
    rospy.init_node('mobot_tf_listener')

    listener = tf.TransformListener()

    rospy.wait_for_service('gazebo_msgs/SpawnModel')
    spawner = rospy.ServiceProxy('gazebo_msgs/SpawnModel', gazebo_msgs.srv.SpawnModel)
    spawner(4, 2, 0, 'mobot2')

    mobot_vel = rospy.Publisher('mobot2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/mobot2', '/mobot1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        mobot_vel.publish(cmd)

        rate.sleep()
