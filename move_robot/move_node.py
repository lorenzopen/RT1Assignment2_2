import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time

class MoveRobotNode(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.sub_odom = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.pub_vel = self.create_publisher(Twist, '/cmd_vel', 10)

        self.linear = 0.0
        self.last_linear = 0.0
        self.angular = 0.0
        self.last_angular = 0.0
                
        self.get_velocity()

    def get_velocity(self):
        while rclpy.ok():
            try:
                user_input = input("Enter 'linear angular' to set velocities: ")
                self.linear, self.angular = map(float, user_input.split())
                self.move_robot()
            except ValueError:
                self.get_logger().error("Invalid input. Please enter two numbers separated by a space.")


    def odom_callback(self, msg):
        if (msg.pose.pose.position.x > 9.0 or msg.pose.pose.position.x < 1.0 or msg.pose.pose.position.y < 1.0 or msg.pose.pose.position.y > 9.0):
            self.get_logger().warn("Boundary reached! Stopping and reversing.")
            self.stop()
            self.reverse_robot()

    def move_robot(self):
        msg = Twist()
        msg.linear.x = self.linear
        msg.angular.z = self.angular
        self.pub_vel.publish(msg)

        self.last_linear = self.linear
        self.last_angular = self.angular

        time.sleep(1.0)
        self.stop()


    def stop(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.pub_vel.publish(msg)
        
    def reverse_robot(self):
        msg = Twist()
        msg.linear.x = 0.2 * -self.last_linear
        msg.angular.z = 0.2 * -self.last_angular
        self.pub_vel.publish(msg)

        time.sleep(1.0)
        self.stop()


def main(args=None):
    rclpy.init(args=args)
    vel_pub = MoveRobotNode()
    try:
        rclpy.spin(vel_pub)
    except KeyboardInterrupt:
        vel_pub.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
