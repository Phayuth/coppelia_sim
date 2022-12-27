#! /usr/bin/env python

import rospy
import numpy as np
from trajectory_msgs.msg import JointTrajectory , JointTrajectoryPoint

rospy.init_node("planning")

pub = rospy.Publisher("/ur5_copp/joint_command", JointTrajectory, queue_size = 10)

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    
    joint = JointTrajectory()
    joint.header.stamp = rospy.Time.now()
    joint.header.frame_id = ''
    joint.joint_names = ['elbow_joint', 'shoulder_lift_joint', 'shoulder_pan_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

    point = JointTrajectoryPoint()
    point.positions = [1, 2, 3, 4, 5, 6]
    point.velocities = []
    point.accelerations = []
    point.effort = []
    point.time_from_start = rospy.Duration(1)

    joint.points.append(point)

    
    pub.publish(joint)
    rate.sleep()