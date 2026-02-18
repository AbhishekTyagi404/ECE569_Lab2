# ECE 569 Spring 2026  
## Lab 2 – URDF, XACRO, and ROS2 Packages  

The instructions for Lab 2 are provided in the official course GitHub repository.  
This repository contains my complete implementation of Lab 2, including Steps 1 through 4.

---

## Student Information

**Name:** Abhishek Tyagi  
**Email:** tyagi55@purdue.edu  

---

## Repository Structure

This repository contains all lab steps organized inside the Lab2 folder.  
The final ROS2 package implementation is located inside Step4.

```
ECE569_Lab2/
├── Step1/
├── Step2/
├── Step3/
├── Step4/
│   └── ur3e_on_table/
└── README.md
```

---

## Step 1 – URDF Modeling

Located in:

```
Step1/
```

Includes:
- rrbot URDF
- r3bot URDF
- table URDF
- Corresponding launch files
- RViz configuration files

This step focused on:
- Creating links and joints in URDF
- Understanding fixed and revolute joints
- Visualizing robots in RViz
- Building simple kinematic chains

---

## Step 2 – XACRO and Modular Robot Descriptions

Located in:

```
Step2/
```

Includes:
- XACRO macros for robot and table
- Parameterized robot instantiation
- Prefix handling for multi-robot setups
- Robotics lab environment configuration

This step focused on:
- Using XACRO macros
- Parameter passing
- Avoiding duplicate link and joint names
- Modular robot modeling

---

## Step 3 – Publishing Joint States

Implemented inside:

```
Step4/ur3e_on_table/
```

Custom ROS2 nodes created:

- `joint_publisher_test.py`
- `joint_publisher_lissajous.py`

These nodes publish `sensor_msgs/msg/JointState` messages to `/joint_states`.

Verified using:

```
ros2 topic list -t
ros2 topic echo /joint_states
ros2 node list
```

RViz was used to visualize motion trajectories with tool0 trail enabled.

---

## Step 4 – Pick and Place Motion

Implemented inside:

```
Step4/ur3e_on_table/joint_publisher_pick_place.py
```

Features:
- Two joint vectors p1 and p2 in R6
- Linear interpolation between joint positions
- 20 second motion cycle
- Repeating pick and place trajectory
- Visualization with tool0 trail in RViz

Launch file:

```
pick_place_ur3e_on_table.launch.py
```

---

## ROS2 Package: ur3e_on_table

Located in:

```
Step4/ur3e_on_table/
```

Structure:

```
ur3e_on_table/
├── launch/
│   ├── view_ur3e_on_table.launch.py
│   ├── test_ur3e_on_table.launch.py
│   ├── lissajous_ur3e_on_table.launch.py
│   └── pick_place_ur3e_on_table.launch.py
│
├── resource/
│   └── lissajous.csv
│
├── urdf/
│   └── ur3e_on_table.urdf.xacro
│
├── ur3e_on_table/
│   ├── __init__.py
│   ├── joint_publisher_test.py
│   ├── joint_publisher_lissajous.py
│   └── joint_publisher_pick_place.py
│
├── package.xml
└── setup.py
```

---

## Build Instructions

From workspace root:

```
colcon build
source install/setup.bash
```

---

## Run Instructions

### View UR3e Robot
```
ros2 launch ur3e_on_table view_ur3e_on_table.launch.py
```

### Test Curve
```
ros2 launch ur3e_on_table test_ur3e_on_table.launch.py
```

### Lissajous Curve
```
ros2 launch ur3e_on_table lissajous_ur3e_on_table.launch.py
```

### Pick and Place Motion
```
ros2 launch ur3e_on_table pick_place_ur3e_on_table.launch.py
```

In RViz:

```
RobotModel → Links → tool0 → Enable Show Trail
```

---

## Submission Notes

All required screenshots for:
- UR3e on table  
- Test curve  
- Lissajous curve  
- Pick and place motion  

are included in the lab report submitted to Gradescope.

This repository contains the complete implementation for Lab 2.

