L_FRONT = [1, 3, 5]
R_FRONT = [0, 2, 4]
L_REAR = [10, 8, 6]
R_REAR = [11, 9, 7]

BODY_MOTOR_MAP = {
            "all": L_FRONT + R_FRONT + L_REAR + R_REAR,
            "l_front": L_FRONT,
            "r_front": R_FRONT,
            "l_rear": L_REAR,
            "r_rear": R_REAR
        }

JOINT_MOTOR_MAP = {
            "front_left_shoulder": 5,
            "front_left_knee": 3,
            "front_left_wrist": 1,
            "front_right_shoulder": 4,
            "front_right_knee": 2,
            "front_right_wrist": 0,
            "rear_left_shoulder": 6,
            "rear_left_knee": 8,
            "rear_left_wrist": 10,
            "rear_right_shoulder": 7,
            "rear_right_knee": 9,
            "rear_right_wrist": 11
        }

JOINT_CENTERS = {
            "front_left_wrist": 2.2,
            "front_right_wrist": 0.17,
            "front_left_knee": 1.13,
            "front_right_knee": 1.18,
            "front_left_shoulder": 1.18,
            "front_right_shoulder": 1.13,
            "rear_left_wrist": 2.1,
            "rear_right_wrist": 0.1,
            "rear_left_knee": 1.2,
            "rear_right_knee": 1.13,
            "rear_left_shoulder": 1.25,
            "rear_right_shoulder": 1.13
        }

JOINT_SOFT_LIMITS = {
            "front_left_wrist": [-2.1, 0.1],
            "front_right_wrist": [-0.1, 2.1],
            "front_left_knee": [-1, 1],
            "front_right_knee": [-1, 1],
            "front_left_shoulder": [-1, 0.6],
            "front_right_shoulder": [-0.6, 1],
            "rear_left_wrist": [-2.1, 0.1],
            "rear_right_wrist": [-0.1, 2.1],
            "rear_left_knee": [-1, 1],
            "rear_right_knee": [-1, 1],
            "rear_left_shoulder": [-0.6, 1],
            "rear_right_shoulder": [-1, 0.6]
        }

JOINT_LIMITS = {
            0: {"upper": 130, "lower": 0},
            1: {"upper": 130, "lower": 0},
            2: {"upper": 130, "lower": 0},
            3: {"upper": 130, "lower": 0},
            4: {"upper": 130, "lower": 45},
            5: {"upper": 130, "lower": 45},
            6: {"upper": 130, "lower": 45},
            7: {"upper": 130, "lower": 45},
            8: {"upper": 130, "lower": 0},
            9: {"upper": 130, "lower": 0},
            10: {"upper": 130, "lower": 0},
            11: {"upper": 130, "lower": 0},
        }
