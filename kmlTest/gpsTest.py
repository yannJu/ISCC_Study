#!/usr/bin/env python
import rospy
from sensor_msgs.msg import NavSatFix
import simplekml

pub = None
kml = simplekml.Kml()

def gps(data):
	global pub
	global kml
	latitude = data.latitude
	longitude = data.longitude
	#lst.append(["(lat/ long)", "lt/longt", (latitude, longitude)])
	#print("latitude : {}\nlongitude : {}".format(latitude, longitude))
	kml.newpoint(name="(lat/long)", description = "lt/longt", coords=[(longitude, latitude)])
rospy.init_node('gpsTest')
rospy.Subscriber('gps_front/fix', NavSatFix, gps)

while not rospy.is_shutdown():
	kml.save("/home/user/catkin_ws/src/ublox/gpsTest/src/kmltest.kml")
	pass