#!/usr/bin/env python

import rospy
from kongsberg_em_control.srv import EMControl
from kongsberg_em_control.srv import EMControlRequest
from std_msgs.msg import String

def endoflineCallback(msg):
  em_req = EMControlRequest()
  em_req.requested_mode = int(EMControlRequest.SONAR_REQUEST_INCREMENT_LINE)
  try:
    response = emControl(em_req)
  except rospy.ServiceException as exc:
    print('error:',str(exc))

rospy.init_node('endofline_listener')

emControl = rospy.ServiceProxy('sonar/control', EMControl)

rospy.Subscriber('project11/endofline', String, endoflineCallback)

rospy.spin()
