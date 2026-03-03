\# 🚀 ROS2 + Arduino Serial LED Control



This project demonstrates serial communication between a ROS2 node and an Arduino using UART.



---



\## 🔧 Overview



A custom ROS2 package (`my\_led\_pkg`) sends `"0"` and `"1"` over serial every 1 second (default).



\- `"1"` → LED on pin 13 turns ON  

\- `"0"` → LED on pin 13 turns OFF  



The blink rate is configurable using a ROS2 parameter.



---



\## 🧠 Technologies Used



\- ROS2 (rclpy)

\- PySerial

\- Docker

\- usbipd (USB passthrough in WSL)

\- Arduino (UART communication)



---



\## ⚙️ Parameters



| Parameter   | Description              | Default      |

|------------|--------------------------|-------------|

| time\_period | Blink interval (seconds) | 1.0 |

| port        | Serial port              | /dev/ttyACM0 |

| baud\_rate   | UART speed               | 9600 |



---



\## ▶️ Run the Node



Download `my\_led\_pkg` package and put it inside your workspace's 'src' folder



Inside your workspace (where src exists):



```bash

colcon build

source install/setup.bash

ros2 run my\_led\_pkg blink\_led



---



\## 🔄 Change Blink Speed (Changing ROS2 Parameter)



Here we are modifying the time\_period parameter to change the blink interval:



```bash

ros2 run my\_led\_pkg blink\_led --ros-args -p time\_period:=3.0



---



\## 💡 What I Learned



* Creating custom ROS2 packages
* Serial communication using PySerial
* ROS2 timers \& Duration
* Parameter handling
* USB passthrough with usbipd
* Docker-based ROS2 development
* Integrating ROS2 with real hardware



---

