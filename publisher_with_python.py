#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtlePublisher(Node):

    def __init__(self):
        super().__init__("turtle_publisher")

        # Create publisher
        self.publisher_ = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )

        # Timer to publish commands repeatedly
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.publish_velocity)

        self.get_logger().info("Publisher Node Started")

    def publish_velocity(self):

        msg = Twist()

        msg.linear.x = 2.0
        msg.angular.z = 1.0

        self.publisher_.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = TurtlePublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()