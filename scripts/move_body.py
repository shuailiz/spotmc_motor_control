#!/usr/bin/python3
import rospy
import time

from spotmicro_motor_control.servo_controller import BodyState
from spotmicro_motor_control.servo_controller import ServoController


if __name__ == '__main__':
    rospy.init_node("move_body")

    servo_control = ServoController()
    body_state_test = BodyState()
    body_state_pre = BodyState()
    body_state_stand = BodyState()
    body_state_rest = BodyState()

    body_state_test.groups = ["r_rear"]
    body_state_test.positions = [[115, 40, 65]]
    #servo_control.move_to_body_state(body_state_test)

    body_state_stand.groups = ["l_front", "r_rear", "l_rear", "r_front"]
    body_state_stand.positions = [[15, 65, 65], [115, 40, 65], [15, 90, 65], [115, 65, 65]]
    servo_control.move_to_body_state(body_state_stand)

    body_state_rest.groups = ["l_front", "r_rear", "l_rear", "r_front"]
    body_state_rest.positions = [[0, 65, 65], [130, 75, 65], [0, 55, 65], [130, 65, 65]]
    #servo_control.move_to_body_state(body_state_rest)

    #body_state_stand.groups = ["l_front", "r_rear", "l_rear", "r_front"]
    #body_state_stand.positions = [[55, 65, 75], [125, 65, 75], [55, 65, 105], [125, 65, 105]]

    #servo_control.move_to_body_state(body_state_rest)
    #time.sleep(3)
    #servo_control.move_to_body_state(body_state_pre)
    #time.sleep(2)
    #servo_control.move_to_body_state(body_state_stand)
    #time.sleep(3)
    #servo_control.move_to_body_state(body_state_pre)
