#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState

rospy.init_node("joint_publisher")
jointstate = JointState()

try:
  pub = rospy.Publisher("/joint_states", JointState, queue_size=10)
  rate_mgr = rospy.Rate(10)  # 10hz
  print "Run!"
  while not rospy.is_shutdown():
    jointstate.header.stamp = rospy.Time.now()
    for i in range(0, 7):
      jointstate.name.append("joint_" + str(i))
      jointstate.position.append(i)

    jointstate.velocity = []
    jointstate.effort = []

    pub.publish(jointstate)
    rate_mgr.sleep()  # this has rospy.spin()
except rospy.ROSInterruptException:
  pass