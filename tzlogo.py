#!/usr/bin/env python3
import sys
import traceback
import rospy
import math
from multiprocessing.resource_sharer import stop
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from time import sleep


def pose_callback(pose: Pose):
    vel = Twist()
    pi=3.1415926535897
    speed=1
    radius=1
    angspeed=1
    relangle=90*2*pi/360
    vel.linear.x=0
    vel.linear.y=0
    vel.linear.z=0
    vel.angular.x=0
    vel.angular.y=0
    vel.angular.z=0
    list1=[(3,10),(5,9),(5,7),(6,7),(7,5),(4,5),(3,6)]
    while not rospy.is_shutdown():
        pub.publish(vel)
        for i in range(1,1+i):
            x1=list1[i][0]
            y1=list1[i][1]
            x2=list1[i+1][0]
            y2=list1[i+1][1]
            m=(y2-y1)/(x2-x1)
            th=math.atan(m)
            t0=rospy.Time.now().to_sec
            vel.angular.z=1
            while(curangle<th):
                pub.publish(vel)
                t1=rospy.Time.now().to_sec()
                curangle=angspeed*(t1-t0)
            if curangle==th:
                vel.angular.z=0
                vel.linear.x=1
            if pose.x==x2 and pose.y==y2:
                vel.linear.x=0
                

    


   




    #pub.publish(cmd)


def main():
    print("	We are doing Successfully!")


if name == "main":
    rospy.init_node("task_0")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rospy.loginfo("Node has been started")
    rate = rospy.Rate(10)

    rospy.spin()
