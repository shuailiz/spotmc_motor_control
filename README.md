# Spotmicro Motor Control
This package controls with the servos using a Raspberry Pi 4 with an [Adafruit 16-Channel servo hat](https://www.adafruit.com/product/2327). The current servos are:
*  [25kg servo](https://www.amazon.com/gp/product/B0882W5P22/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) for all shoulder and elbow joints.
* [35kg servo](https://www.amazon.com/gp/product/B07SBYZ4G5/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) for all wrist joints.

The servos are all 180 degrees range servos. 

This package requires [Adafruit_CircuitPython_ServoKit](https://github.com/adafruit/Adafruit_CircuitPython_ServoKit) and ROS melodic installed. The package also contains constants that define the servo related properties including:
* Joint limits
* Joint centers
* Servo <-> joint mapping