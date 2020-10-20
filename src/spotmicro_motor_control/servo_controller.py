import numpy as np
import time

from spotmicro_motor_control.constants import BODY_MOTOR_MAP
from spotmicro_motor_control.constants import JOINT_MOTOR_MAP
from spotmicro_motor_control.constants import JOINT_LIMITS
from spotmicro_motor_control.constants import JOINT_CENTERS

import rospy
from adafruit_servokit import ServoKit


class BodyState(object):

    groups = None
    positions = None

class ServoController(object):
    NUM_OF_SERVOS = 12
    MIN_PULSE_WIDTH = 771
    MAX_PULSE_WIDTH = 2740

    def __init__(self):
        self.servo_kit = ServoKit(channels=16)
        for i in range(self.NUM_OF_SERVOS):
            self.servo_kit.servo[i].set_pulse_width_range(self.MIN_PULSE_WIDTH,
                                                          self.MAX_PULSE_WIDTH)

    def validate_motor_target(self, target, motor_id, degree=True):
        if not degree:
            target = target / np.pi * 180
        if target > JOINT_LIMITS[motor_id]["upper"] or \
                target < JOINT_LIMITS[motor_id]["lower"]:
            rospy.logerr("Target %f is out of the joint limits" % target)
            return False
        return True

    def move_single_joint_radian(self, joint_name, joint_value_radian):
        motor_id = JOINT_MOTOR_MAP[joint_name]
        joint_value_radian += JOINT_CENTERS[joint_name]
        self.move_single_motor_radian(motor_id, joint_value_radian)

    def move_single_motor_degree(self, motor_id, angle_degree):
        if motor_id >= self.NUM_OF_SERVOS:
            raise("Please use a motor id between 0 and %d"%self.NUM_OF_SERVOS)

        self.validate_motor_target(angle_degree, motor_id)
        rospy.loginfo("ID is %d and angle is %f", motor_id, angle_degree)
        self.servo_kit.servo[motor_id].angle = angle_degree
        time.sleep(0.01)

    def move_single_motor_radian(self, motor_id, angle_radian):
        angle_degree = angle_radian * 180 / np.pi
        self.move_single_motor_degree(motor_id, angle_degree)

    def move_motor_set(self, motor_id_array, angle_set_array, degree=True):
        assert len(motor_id_array) == len(angle_set_array)

        for motor_id, angle in zip(motor_id_array, angle_set_array):
            if degree:
                self.move_single_motor_degree(motor_id, angle)
            else:
                self.move_single_motor_radian(motor_id, angle)

    def move_to_body_state(self, body_state, degree=True):
        for group, position in zip(body_state.groups, body_state.positions):
            if group not in BODY_MOTOR_MAP:
                raise("Group name %s not in known body map" % group)

            if len(BODY_MOTOR_MAP[group]) != len(position):
                raise("The motor position length is invalid!")

            self.move_motor_set(BODY_MOTOR_MAP[group], position)
