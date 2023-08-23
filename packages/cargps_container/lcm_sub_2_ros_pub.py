from dt_communication_utils import DTCommunicationGroup
from std_msgs.msg import Float32MultiArray
import rospy
import os
from duckietown.dtros import DTROS, NodeType

class Car_Publisher(DTROS):
    def __init__(self, node_name):
        super(Car_Publisher, self).__init__(node_name=node_name,node_type=NodeType.GENERIC)
        self.pub = rospy.Publisher('coordinates',Float32MultiArray,queue_size=10)

    def run(self,x,y):
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            msg_data = [x,y]
            message = Float32MultiArray(data=msg_data)
            self.pub.publish(message)
            rate.sleep()


group = DTCommunicationGroup('nuc_group', Float32MultiArray)
node = Car_Publisher(node_name='car_publisher')
print('running the subscriber')

def callback(message, header):
    print(message.data)
    x = None
    y = None
    data = message.data
    car_num = os.environ.get('CAR_NUMBER')
    counter = 0
    for num in data:
        if num == car_num:
            x = data[counter + 1]
            y = data[counter + 2]
        counter += 1
    node.run(x,y)
    


if __name__ == '__main__':
    subscriber = group.Subscriber(callback)



