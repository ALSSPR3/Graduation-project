#!/usr/bin/env python2

import rospy

class detector:
    DETECTOR_TOPIC = "/darknet_ros/bounding_boxes"
    stop_sign_check = false
    DEBUG = False

    def __init__(self):
	self.detector_subcriber = rospy.Subscriber(self.DETECTOR_TOPIC, DETECTOR_TOPIC, self.detectorCallback)

    def detectorCallback(self, data):
	if stop_sign_check == false 
		stop_sign_check = true
		for each in data.bounding_boxes:
			if each.Class == "person":
				print "check true"


if __name__ == "__main__":
    rospy.init_node("Detector")
    Detector = detector()
    rospy.spin()
