import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.duration import Duration

import serial
import time

class BlinkLED(Node):
    def __init__(self):
        super().__init__("blink_led")
        self.declare_parameter("time_period",1.0)
        self.declare_parameter("port","/dev/ttyACM0")
        self.declare_parameter("baud_rate",9600)

        self.state = "0"

        self._timer_period = self.get_parameter("time_period").value
        self._port = self.get_parameter("port").value
        self._baud_rate = self.get_parameter("baud_rate").value

        self._serial = serial.Serial(self._port,self._baud_rate, write_timeout=0.1)
        time.sleep(2)

        self._timestamp = self.get_clock().now()

        self._timer = self.create_timer(0.1, self._blink_callback)
    
    def _blink_callback(self):
        elapsed = self.get_clock().now() - self._timestamp
        if elapsed >= Duration(seconds=self._timer_period):
            self._timestamp = self.get_clock().now()
            if self.state == "1":
                self._serial.write((self.state).encode())
                self.get_logger().info(f"state = {self.state}")
                self.state = "0"
            else:
                self._serial.write((self.state).encode())
                self.get_logger().info(f"state = {self.state}")
                self.state = "1"
    
    def serial_close(self):
        self._serial.close()
            

def main(args=None):
    try:
        rclpy.init()
        node = BlinkLED()
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        if node is not None:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
        node.serial_close()

if __name__ == "__main__":
    main()

