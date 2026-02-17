from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command

def generate_launch_description():

    robot_description_content = Command(
        ['xacro ', 'table.urdf.xacro']
    )

    robot_description = {'robot_description': robot_description_content}

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[robot_description]
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])

