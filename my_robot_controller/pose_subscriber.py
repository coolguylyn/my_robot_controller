#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64

class PoseSubscriberNode(Node):
    def __init__(self):
        super( ).__init__("pose_subscriber")
        self.pose_subscriber_ = self.create_subscription(
            Odometry, "/gx5/nav/odom", self.pose_callback, 1000)
        self.comp_subscriber_ = self.create_subscription(
            Float64, "/gx5/compass", self.compass_callback, 1000)
    
    def pose_callback(self, msg: Odometry):
       self.get_logger().info(str(msg.pose.pose.position.x) + " Lat")
       self.get_logger().info(str(msg.pose.pose.position.y) + " Lon")
       
    def compass_callback(self, msg: Float64):
       self.get_logger().info(str(msg.data) + " Rotation")

    


def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()