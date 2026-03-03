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



Inside your workspace:



```bash

colcon build

source install/setup.bash

ros2 run my\_led\_pkg blink\_led

