#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sstream>

void callback(const std_msgs::String::ConstPtr &request)
{
	ROS_INFO("I knows [%s]", request->data.c_str());
}

int main(int argc,char** argv)
{
	ros::init(argc,argv,"subscriber_node");
	ros::NodeHandle n;
	ros::Subscriber sub = n.subscribe("/aungthiha",1000 , callback);
	ros::spin();
}
