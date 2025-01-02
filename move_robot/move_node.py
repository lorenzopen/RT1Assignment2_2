import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('move_robot')
    pub = node.create_publisher(Twist, '/cmd_vel', 10)
    node.get_logger().info('MoveRobotNode has been started.')

    def move_robot(linear, angular):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        pub.publish(msg)
        node.get_logger().info(f'Published linear={linear}, angular={angular}')

    try:
        while rclpy.ok():
            linear = float(input('Enter linear velocity: '))
            angular = float(input('Enter angular velocity: '))
            move_robot(linear, angular)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()