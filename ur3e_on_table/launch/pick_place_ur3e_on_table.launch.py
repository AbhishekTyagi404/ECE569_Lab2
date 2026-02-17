from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    robot_description_content = Command([
        'xacro ',
        PathJoinSubstitution([
            FindPackageShare('ur3e_on_table'),
            'urdf',
            'ur3e_on_table.urdf.xacro'
        ])
    ])

    return LaunchDescription([

        Node(
            package='ur3e_on_table',
            executable='pick_place',
            output='screen'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description_content}]
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        ),
    ])

