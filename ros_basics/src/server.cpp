#include <ros/ros.h>
#include <ros_basics/AddTwoInts.h>


bool add(ros_basics::AddTwoInts::Request &req,
		 ros_basics::AddTwoInts::Response &res)
{
	res.result = req.a + req.b +req.c;
	ROS_INFO("SENT!");
	ROS_INFO("Multiplication is [%d]", (int)res.result);
	return true;
}


int main(int argc, char ** argv)
{
	ros::init(argc,argv, "server_node");
	ros::NodeHandle n;
	ros::ServiceServer service = n.advertiseService ("add_two_integers_service",add);
	ROS_INFO("Ready to add three integers!");
	ros::spin();
	

}	