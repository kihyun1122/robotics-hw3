#!/usr/bin/env python
import rospy
from common_msgs.msg import blank
from common_msgs.srv import Coord2Goal, Coord2GoalRequest

rospy.init_node('blank_publisher')
pub = rospy.Publisher('custom_msg', blank, queue_size=1)

coord_requester = rospy.ServiceProxy('coord_to_goal', Coord2Goal)

rate = rospy.Rate(2)
count = 0
coord_count = 0
pub_color = blank()
color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
coordinator_list = [(100, 200, 300), (15, 1, 30), (1993, 11, 22)]

while not rospy.is_shutdown():
    if count > 2:
        count = 0
    pub_color.rgb_data.r = color_list[count][0]
    pub_color.rgb_data.g = color_list[count][1]
    pub_color.rgb_data.b = color_list[count][2]
    pub_color.xyz_data.x = coordinator_list[count][0]
    pub_color.xyz_data.y = coordinator_list[count][1]
    pub_color.xyz_data.z = coordinator_list[count][2]
    pub_color.int_data.data = count
    
    count += 1
    pub.publish(pub_color)
    print "published data for Red   : %d" % pub_color.rgb_data.r
    print "published data for Green : %d" % pub_color.rgb_data.g
    print "published data for Blue  : %d" % pub_color.rgb_data.b
    print ""
    print "published data for Coor X: %d" % pub_color.xyz_data.x
    print "published data for Coor Y: %d" % pub_color.xyz_data.y
    print "published data for Coor Z: %d" % pub_color.xyz_data.z
    print ""
    print "published data for New_r : %d" % pub_color.int_data.data
    print "published data for New_b : %d" % pub_color.int_data.data
    print "published data for New_g : %d" % pub_color.int_data.data
    print ""
    print "Pub finished"
    print ""

    coord_count += 1
    if coord_count % 5 == 0:
        #print "coord_count : ", coord_count
        if coord_count > 150:
            coord_count = 0
        req = Coord2GoalRequest(x_re=coord_count, y_re=coord_count*2, z_re=coord_count)
        res = coord_requester(req)
        print "Moved  coordinates : x: ", req.x_re, " y: ", req.y_re, " z: ", req.z_re
        print "Remain coordinates : x: ", res.x, " y: ", res.y, " z: ", res.z
    rate.sleep()

