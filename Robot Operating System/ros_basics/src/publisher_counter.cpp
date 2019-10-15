#include <ros/ros.h>
#include <std_msgs/Int32.h>
#include <sstream>

int main(int argc , char** argv)
{
	ros::init(argc,argv,"counterpub_node");
	ros::NodeHandle n;
	ros::Publisher pub=n.advertise<std_msgs::Int32>("/counter",1000);
	ros::Rate r(1);
	std_msgs::Int32 count;
	count.data = 0;

	while(ros::ok())
	{
		count.data+=1;
		pub.publish(count);
		ros::spinOnce();
		r.sleep();
	}
	return 0;
}