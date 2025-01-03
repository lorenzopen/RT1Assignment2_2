import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MoveRobotNode(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.get_velocity()

        


    def get_velocity(self):
        try:
            while rclpy.ok():
                user_input = input("Enter 'linear angular' to set velocities: ")
                try:
                    self.linear, self.angular = map(float, user_input.split())
                    break
                except ValueError:
                    self.get_logger().error("Invalid input. Please enter two numbers separated by a space.")
        except KeyboardInterrupt:
            pass

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.linear
        msg.angular.z = self.angular
        self.pub.publish(msg)

        time.sleep(1.0)  # 1 second
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.pub.publish(msg)
        self.get_velocity()

def main(args=None):
    rclpy.init(args=args)
    vel_pub = MoveRobotNode()
    rclpy.spin(vel_pub)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
