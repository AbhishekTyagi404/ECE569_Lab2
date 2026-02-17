import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from ament_index_python.packages import get_package_share_directory
import numpy as np
import os

class JointPublisherLissajous(Node):

    def __init__(self):
        super().__init__('joint_publisher_lissajous')

        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.i = 0

        # Proper way to get installed resource path
        pkg_share = get_package_share_directory('ur3e_on_table')
        csv_file = os.path.join(pkg_share, 'resource', 'lissajous.csv')

        self.get_logger().info(f'Loading CSV from: {csv_file}')

        # Use genfromtxt instead of loadtxt
        self.joint_data = np.genfromtxt(
            csv_file,
            delimiter=',',
            skip_header=1
        )

        if self.joint_data.ndim == 1:
            self.joint_data = np.expand_dims(self.joint_data, axis=0)

        self.data_length = self.joint_data.shape[0]
        self.get_logger().info(f'Loaded {self.data_length} rows')

    def timer_callback(self):

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

        msg.position = self.joint_data[self.i, 1:7].tolist()

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing index {self.i}')

        self.i += 1
        self.i %= self.data_length


def main(args=None):
    rclpy.init(args=args)
    node = JointPublisherLissajous()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

