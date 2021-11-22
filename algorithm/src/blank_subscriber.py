#!/usr/bin/env python
import rospy
from common_msgs.msg import blank

def callback(msg):
    red = msg.rgb_data.r
    blue = msg.rgb_data.b
    green = msg.rgb_data.g
    coor_x = msg.xyz_data.x
    coor_y = msg.xyz_data.y
    coor_z = msg.xyz_data.z
    count = msg.int_data.data
    new_r = count * coor_x
    new_b = count * coor_y
    new_g = count * coor_z
    
    print "data for Red   : %d" % red
    print "data for Green : %d" % green
    print "data for Blue  : %d" % blue
    print ""
    print "data for Coor_X: %d" % coor_x
    print "data for Coor_Y: %d" % coor_y
    print "data for Coor_Z: %d" % coor_z
    print ""
    print "data for int : %d" % count
    print ""
    print "data for New : %d" % new_r
    print "data for New : %d" % new_b
    print "data for New : %d" % new_g
    print "Sub finished"

rospy.init_node('blank_subscriber')
sub = rospy.Subscriber('custom_msg', blank, callback)

rospy.spin()
