#!/usr/bin/env python3
#-*- coding:utf-8 -*-	# 한글 주석을 달기 위해 사용한다.


''' azure에서 보내는 publish 정보
        std_msgs::Float32 msg;
        msg.data = 0;
        pub.publish(msg);

TrackerNode::TrackerNode(ros::NodeHandle& _nh)
{
	nh=_nh;
	lengthPub = nh.advertise<std_msgs::Float32>("length",1000);	
}


OpenCR 에서 보내는 정보     

ros::Publisher sceinaro_make("bookcase_num",  &moter_num)
std_msgs::String moter_num //string type으로 bookcase_num topic날림

'''

import rospy
from std_msgs.msg import Float32, String, Int32


class monitor:
    def __init__(self):
        rospy.init_node('monitoring_node', anonymous=True)


        self.height_threshold = rospy.get_param('~height_threshold')

        ###############################
        ####### Make Subscriber #######
        ###############################
        
        self.length_subscriber = rospy.Subscriber(
            name="length", data_class=Float32, callback=self.length_callback)

        self.ac_subscriber = rospy.Subscriber(
            name="ac_information", data_class=String, callback=self.ac_callback)

        self.bookcase_subscriber = rospy.Subscriber(
            name="bookcase_num", data_class=String, callback=self.bookcase_callback)
        
        self.count_subscriber = rospy.Subscriber(
            name="count", data_class=Int32, callback=self.count_callback)

        self.rate = rospy.Rate(30) # 0.5hz

    def length_callback(self,msg): #기본 argument는 구독한 메세지 객체 
        #callback : topic이 발행되는 이벤트가 발생하였을 때 event lisner함수를 콜백함수로 요구
        self.data = msg
        if int(msg.data) == 0:
            rospy.loginfo("사람이 인식되지 않음")
            self.ac = "None"
        elif int(msg.data) >= self.height_threshold:
            rospy.loginfo("adult")
            self.ac = "adult"
        else:
            rospy.loginfo("child")
            self.ac = "child"
        rospy.loginfo(self.ac)
        self.publisher.publish(self.ac)
        #rospy.loginfo("ac_publisher action")
        

    def ac_callback(self,msg): #ac를 인식하는 부분
        #callback : topic이 발행되는 이벤트가 발생하였을 때 event lisner함수를 콜백함수로 요구
        self.ac = msg.data
        #rospy.loginfo(self.ac)
        #self.publisher.publish(self.ac)
    
    def bookcase_callback(self,msg):
        self.bookcase = msg.data
        #rospy.loginfo(self.bookcase)

    def ccount_callback(self,msg):
        self.count = msg.data
        #rospy.loginfo(self.count)
        



    def acpub_azsub_action(self):
        while not rospy.is_shutdown(): #-> c++에서 ros.ok() 느낌
            #rospy.loginfo(rospy.get_time())
            self.rate.sleep() #100hz가 될때 까지 쉬기

            




if __name__ == '__main__':
    try:
        h = height()
        h.acpub_azsub_action()
    except rospy.ROSInterruptException:
        pass
