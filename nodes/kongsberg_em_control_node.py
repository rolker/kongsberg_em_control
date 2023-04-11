#!/usr/bin/env python3

from kongsberg_em_control.srv import *
import rospy
import kongsberg_em_control.em

sonar = None

def handle_em_command(req):
    if req.requested_mode == EMControlRequest.SONAR_REQUEST_STOP_PINGING:
        sonar.stopPinging()
        return EMControlResponse("ok")
    if req.requested_mode == EMControlRequest.SONAR_REQUEST_START_PINGING:
        sonar.startPinging()
        return EMControlResponse("ok")
    if req.requested_mode == EMControlRequest.SONAR_REQUEST_START_LINE:
        sonar.startLine(req.line_number)
        return EMControlResponse("ok")
    if req.requested_mode == EMControlRequest.SONAR_REQUEST_INCREMENT_LINE:
        sonar.incrementLine()
        return EMControlResponse("ok")
    return EMControlResponse("unknown mode")


def EMControlServer():
    global sonar

    rospy.init_node('EMControl')

    host = rospy.get_param('sonar/host','localhost')
    model = rospy.get_param('sonar/model','2040')
    
    sonar = kongsberg_em_control.em.EM(host,str(model))
    
    s = rospy.Service('sonar/control',EMControl, handle_em_command)
    s.spin()
    
    
EMControlServer()
