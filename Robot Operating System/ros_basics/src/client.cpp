#include <ros/ros.h>
#include <ros_basics/AddTwoInts.h>

int main(int argc , char** argv){
	ros::init(argc,argv,"client_node");
	ros::NodeHandle n;
	ros::service::waitForService("add_two_integers_service"); 
	ros::ServiceClient client=n.serviceClient<ros_basics::AddTwoInts>("add_two_integers_service");
	ros::Rate r (10);
	ros_basics::AddTwoInts srv;
	srv.request.a = 3;
	srv.request.b = 4;
	srv.request.c = 5;
	while(ros::ok()){
		if(client.call(srv)){
			ROS_INFO("The answer is : %d", (int)srv.response.result);
			r.sleep();
		}
		else{
			ROS_INFO("Fail to call service multiply_3_ints");
			return 1;
		}
	}
	return 0;
}
