# Duckietown GPS Car Container

This repo creates a docker container that is compatible with the Duckiebots provided by Duckietown. It is the recieving end of the gps system created for BYU's ECEN 433 class. 

It uses LCM  through the dt-communications-utils library to recieve messages from the GPS system over wifi. Those messages are then sorted according to the car number set in the bot. X,Y coordinates are then published over ROS to the rest of the Duckiebot.

This repo was based on the duckietown repo found [here](https://github.com/duckietown/template-ros).


## How to use it

### 1. Clone this repository

Download this repository onto a computer that is able to communicate with the duckiebots over network and has the dt shell installed.

### 2. Edit Dockerfile

Open up the Dockerfile, and make changes to line 51. This variable needs to be set to match the number of Apriltag on your duckiebot. This number should be a float type. So if you have tag #1 on your Duckiebot, then the variable needs to be set as 1.0

