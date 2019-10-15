#include <ros/ros.h>
#include <std_msgs/Int32.h>


void callback(const std_msgs::Int32::ConstPtr& msg)
{
  ROS_INFO("%d", msg->data);
}

int main(int argc,char**argv)
{
	ros::init(argc,argv,"countersub_node");
	ros::NodeHandle n;
	ros::Subscriber sub=n.subscribe("/counter",1000,callback);
	ros::spin();
	return 0;
}