from dt_communication_utils import DTCommunicationGroup
from std_msgs.msg import Float32MultiArray
import rospy
import os
from duckietown.dtros import DTROS, NodeType

class Car_Publisher(DTROS):
    def __init__(self,node_name):
        self.group = DTCommunicationGroup('nuc_group', Float32MultiArray)
        super(Car_Publisher, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        self.pub = rospy.Publisher('/car_coordinates',Float32MultiArray,queue_size=10)
        self.car_num = os.environ.get('CAR_NUMBER')
        self.sub = self.group.Subscriber(self.callback) 

    def callback(self,message,header):
        for i in range(len(message.data)):
            if message.data[i] == float(self.car_num):
                ros_message = Float32MultiArray()
                ros_message.data = [message.data[i+1],message.data[i+2]]
                self.pub.publish(ros_message)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Car_Publisher('car_coordinates_node')
    node.run()

#start this node in the car with 
# docker run -it -e CAR_NUMBER=7.0 --network host duckietown/car_container:v2-arm64v8 bash

