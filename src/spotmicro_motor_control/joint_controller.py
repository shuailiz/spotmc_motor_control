import rospy
from sensor_msgs.msg import JointState
from spotmicro_motor_control.servo_controller import ServoController
from spotmicro_motor_control.constants import JOINT_MOTOR_MAP


class SpotJointController(object):
    def __init__(self):
        self.joint_state_pub = rospy.Publisher("joint_states_real",
                                               JointState,
                                               queue_size=1)
        self.joint_control_sub = rospy.Subscriber("spotmicro/joint_controller",
                                                  JointState,
                                                  self.joint_control_cb)
        self.servo_ctrl = ServoController()

        self.joint_names = JOINT_MOTOR_MAP.keys()
        self.joint_command = None
        self.loop_rate = rospy.Rate(50)

    def joint_control_cb(self, msg):
        self.joint_command = msg

    def run(self):
        while not rospy.is_shutdown():
            if self.joint_command is not None:
                self.joint_state_pub.publish(self.joint_command)
                for joint_name, joint_value in zip(self.joint_command.name,
                                                   self.joint_command.position):
                    self.servo_ctrl.move_single_joint_radian(joint_name, joint_value)
            self.loop_rate.sleep()

