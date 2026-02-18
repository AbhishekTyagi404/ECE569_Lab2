import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import numpy as np


def linear_interpolate(p1, p2, a):
    return (1 - a) * p1 + a * p2


class JointPublisherPickAndPlace(Node):

    def __init__(self):
        super().__init__('joint_publisher_pick_place')

        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)

        self.timer_period = 0.02
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.t = 0.0

        # REALISTIC JOINT POSITIONS (safe values)
        self.p1 = np.array([-1.7, -1.4, -1.8, -3.0, -0.9, 3.07])
        self.p2 = np.array([-1.2, -0.8, -1.2, -2.5, -0.9, 3.07])

    def timer_callback(self):

        # 20 second cycle
        cycle_time = 20.0
        t_mod = self.t % cycle_time

        if t_mod < 5:
            a = 0.0
        elif t_mod < 10:
            a = (t_mod - 5) / 5
        elif t_mod < 15:
            a = 1.0
        else:
            a = 1.0 - (t_mod - 15) / 5

        p = linear_interpolate(self.p1, self.p2, a)

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [
            'shoulder_pan_joint',
            'shoulder_lift_joint',
            'elbow_joint',
            'wrist_1_joint',
            'wrist_2_joint',
            'wrist_3_joint'
        ]
        msg.position = p.tolist()
        msg.velocity = []
        msg.effort = []

        self.publisher_.publish(msg)

        self.t += self.timer_period


def main(args=None):
    rclpy.init(args=args)
    node = JointPublisherPickAndPlace()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

