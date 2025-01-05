import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class PositionBasedMotion(Node):

    def __init__(self):
        super().__init__('ex1_like')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription_ = self.create_subscription(Odometry,'/odom',self.odometry_listener_callback,10)


def main(args=None):
    rclpy.init(args=args)
    ex1_like = PositionBasedMotion()
    rclpy.spin(ex1_like)
    rclpy.shutdown()

if __name__ == '__main__':
    main()