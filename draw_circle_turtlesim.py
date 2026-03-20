#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class DrawCircle(Node):

    def __init__(self):
        super().__init__("draw_circle_node")

        # Publisher to send velocity commands
        self.publisher_ = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )

        # Timer to publish commands repeatedly
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.move_circle)

        self.get_logger().info("Draw Circle Node Started")

    def move_circle(self):

        msg = Twist()

        # Forward velocity
        msg.linear.x = 2.0

        # Angular velocity (turning)
        msg.angular.z = 1.0

        self.publisher_.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = DrawCircle()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()