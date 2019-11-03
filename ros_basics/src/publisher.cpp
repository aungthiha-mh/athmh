#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sstream>

int main(int argc , char** argv)                  // command-line arguments>>arg-count and arg-vector
{
	ros::init(argc,argv,"publisher_node");        // ROS initialization function
	ros::NodeHandle n;                            // To start-up automatically in roscpp(if program is finished,node is shutdown)for writing nodes
	ros::Publisher pub = n.advertise<std_msgs::String>("/aungthiha",1000);      //Advertise a topic and returns Publisher.This version of advertise is a templated convenience function

	ros::Rate r(1);
	while(ros::ok())
	{
		std_msgs::String msg;
		std::stringstream ss;
		ss << "Hey,I am Aung Thiha !" ;
		msg.data = ss.str();

		ROS_INFO(msg.data.c_str());
		pub.publish(msg);
		ros::spinOnce();
		r.sleep();
	}

	return 0;
}