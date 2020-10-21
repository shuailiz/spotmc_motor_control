#!/usr/bin/python3
import rospy
from spotmicro_motor_control.joint_controller import SpotJointController


if __name__ == '__main__':
    rospy.init_node('spot_joint_control_node')
    rospy.loginfo("Joint controller for spot has been started")
    joint_control = SpotJointController()
    joint_control.run()
