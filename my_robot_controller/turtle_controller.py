#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("The new thing is happening")


def main(args=None):
    rclpy.init(args=args)
    node =  TurtleControllerNode           # Node name goes here
    rclpy.spin(node)   # Use spin if you want the node to keep running
    rclpy.shutdown()

if __name__ == '__main__':
    main()