# ROS2 Learning Notes  
*(Following the Robotics Back-End ROS2, Articulated Robotics, ROS2 Official Documentation, Robotics System Lab ETH Zurich Playlist)*

This repository documents my learning journey of **ROS2 (Robot Operating System 2)** while following the **Robotics Back-End YouTube playlist**.  

The playlist starts with a **clear introduction explaining the ROS ecosystem and architecture**, then gradually moves toward **hands-on practical topics like nodes, topics, services, packages, and building robot applications**.

The goal of this repository is to organize the learning topics and commands so that anyone starting with ROS2 can quickly understand the **basic → intermediate workflow used in robotics development**.

---

# Topics Covered in the Playlist

## 1. Introduction to ROS2
- What is ROS
- What is ROS2
- Why ROS is used in robotics
- ROS architecture overview
- Differences between ROS and ROS2

Subtopics
- Nodes
- Topics
- Services
- Actions
- Messages
- ROS graph

---

# 2. ROS2 Installation & Environment Setup
Topics
- Installing ROS2
- Setting up environment variables
- Verifying ROS installation

Subtopics
- ROS2 CLI
- environment sourcing
- package repositories

Commands

- ros2 --help
- ros2 node list
- ros2 topic list

---

# 3. ROS2 Command Line Tools
Topics
- ROS2 command line interface
- Exploring ROS system

Subtopics
- node commands
- topic commands
- service commands
- interface commands

Commands

- ros2 node list
- ros2 topic list
- ros2 service list
- ros2 interface list
- ros2 pkg list
---

# 4. ROS2 Workspace
Topics
- What is a ROS workspace
- Workspace structure
- Building packages

Subtopics
- src folder
- build folder
- install folder
- log folder

Commands
- mkdir -p ~/ros2_ws/src
- cd ~/ros2_ws
- colcon build
- source install/setup.bash
---

# 5. ROS2 Nodes
Topics
- What is a node
- Running nodes
- Node architecture

Subtopics
- node lifecycle
- node communication
- node execution

Commands

- ros2 run <package_name> <node_name>
ros2 node list
ros2 node info <node_name>
---

# 6. ROS2 Topics
Topics
- Publisher and Subscriber model
- Message communication between nodes

Subtopics
- topic publishing
- topic subscribing
- topic message types

Commands

- ros2 topic list
- ros2 topic echo <topic_name>
- ros2 topic info <topic_name>
- ros2 topic pub <topic_name> <msg_type>

---

# 7. ROS2 Messages
Topics
- Message structure
- Data communication between nodes

Subtopics
- message types
- message fields
- custom messages

Commands

- ros2 interface list
- ros2 interface show <message_type>
---

# 8. Turtlesim Simulator
Topics
- ROS beginner simulator
- Testing node communication

Subtopics
- turtle node
- teleoperation node
- movement commands

Commands

- ros2 run turtlesim turtlesim_node
- ros2 run turtlesim turtle_teleop_key

---


# 9. ROS Graph Visualization

Topics
- Visualizing ROS communication

Subtopics
- node graph
- topic connections
- message flow

Commands

- rqt_graph

# 10. Creating ROS2 Packages
Topics
- Package structure
- Creating Python packages

Commands

- cd ~/ros2_ws/src
ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy
---
# Learning Outcome

After completing these topics, a learner should understand:

- ROS2 architecture
- Node based robot software design
- Communication between nodes
- ROS workspace workflow
- Package creation and building
- Running and debugging ROS nodes

---

⭐ If you found this repository helpful while learning ROS2, feel free to give it a **star or like** for support.