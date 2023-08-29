from dt_communication_utils import DTCommunicationGroup
from std_msgs.msg import Float32MultiArray, MultiArrayLayout, MultiArrayDimension

group = DTCommunicationGroup('nuc_group',Float32MultiArray)

def callback(message, header):
    print(message.data)

subscriber = group.Subscriber(callback)