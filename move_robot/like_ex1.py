import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class PositionBasedMotion(Node):

    def __init__(self):
        super().__init__('ex1_like')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.sub = self.create_subscription(Odometry,'/odom',self.odomcallback,10)

    def odomcallback(self, msg):
        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation

        self.get_logger().info(f"Position: x={position.x:.2f}, y={position.y:.2f}, z={position.z:.2f}")

        vel_msg = Twist()

        if position.x > 9.0: 
            vel_msg.linear.x = 0.5  
            vel_msg.angular.z = 0.5   
        elif position.x < 1.0:
            vel_msg.linear.x = 0.5
            vel_msg.angular.z = 0.5
        else:
            vel_msg.linear.x = 0.5 
            vel_msg.angular.z = 0.0

        self.pub.publish(vel_msg)

def main(args=None):
    rclpy.init(args=args)
    ex1_like = PositionBasedMotion()
    rclpy.spin(ex1_like)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
