#!/usr/bin/env python
import rospy
from common_msgs.msg import blank
from common_msgs.srv import Coord2Goal, Coord2GoalResponse


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
    print ""

def service_callback(request):
    moved_coord_x = request.x_re
    moved_coord_y = request.y_re
    moved_coord_z = request.z_re
    destiny_x = 150
    destiny_y = 300
    destiny_z = 150
    remain_x = destiny_x - moved_coord_x
    remain_y = destiny_y - moved_coord_y
    remain_z = destiny_z - moved_coord_z
    response = Coord2GoalResponse(x=remain_x, y=remain_y, z=remain_z)
    print "Moved  Coordinates x : ", moved_coord_x, " y : ", moved_coord_y, " z : ", moved_coord_z
    print "Remain Coordinates x : ", remain_x, " y : ", remain_y, " z : ", remain_z
    return response


rospy.init_node('blank_subscriber')
sub = rospy.Subscriber('custom_msg', blank, callback)
service = rospy.Service('coord_to_goal', Coord2Goal, service_callback)

rospy.spin()
