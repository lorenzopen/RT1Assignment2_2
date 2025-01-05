# Part 2
This part was on ROS2 and robot_urdf (ros2 branch) pkg, so first of all it's necessary have that cloned and then cloning this pkg.

After starting --> ros2 launch robot_urdf gazebo.launch.py

# mov_node.py : Controlling Robot Motion w/ terminal

## Functionality

The node has the following functionalities:

* **Subscribes to `/odom`:** Receives odometry data (position and orientation) from the robot.
* **Publishes to `/cmd_vel`:** Sends velocity commands to the robot's motion controller based on user input.
* **Basic Motion Control:**
    * Allows user input for linear and angular velocities via terminal.
    * Implements a simple boundary check: If the robot's position exceeds predefined limits, it reverses direction to go back in the 'safe zone'.

1. **Run the Node:** in workspace after 'colcon build' --> ros2 run move_robot move_node
2. **Enter Velocities:** When prompted, enter the desired linear and angular velocities (e.g., "0.2 0.5").
3. ** Robot Behavior:** The robot will move according to the provided velocities and the boundary check.


# like_ex1.py : Auto Pattern Motion

## Functionality
The node performs the following:

* **Subscribes to `/odom`:** Receives odometry data (position and orientation) from the robot.
* **Publishes to `/cmd_vel`:** Sends velocity commands to the robot based on its position.

    - If the robot's x-coordinate is greater than 9.0 meters, it moves forward and turns right.
    - If the robot's x-coordinate is less than -9.0 meters, it moves forward and turns left.
    - Otherwise, it moves forward in a straight line.

## Usage

1. **Run the Node:** in workspace after 'colcon build' --> ros2 run move_robot like_ex1

