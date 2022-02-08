**Simulation in jmavsim**

 -------      ---------      --------      ---------
|       |--->|         |--->|        |--->|        |
|  PX4  |    | MAVLINK |    | MAVROS |    |   ROS  |
|       |<---|         |<---|        |<---|        |
 -------      ---------      --------      --------
 
    In this documentation, we are in ROS:
 
    * ROS launching through UDP connection:
        $ roslaunch mavros px4.launch

            files to check the launching :

    * Check mavros topics publications and subscriptions:
        $ rosnode info /mavros

            **Node**         : (/mavros) node
            **Publications** : topics coming from PX4 so ROS can listen (echo) to:
                $ rostopic echo /mavros/setpoint_raw/target_attitude

            **Subscriptions**: topics going out from ROS so PX4 can listen to. These
            topics can be published from ROS:

                *** However ***************************************************
                *    To control the vehicle in the <offboard> mode, we need to do the following in PX4 side:
                *       pxh>  param set COM_RCL_EXCEPT 7
                *       why? because the PX4 prevents changing to <offboard> mode in the jmavsim
                *       unless some flags and parameters are set.
                *       also check:
                *           pxh> listener vehicle_status_flags
                *
                *    Then we need to takeoff:
                *        pxh> commander arm
                *        (I need to figure out how to do that from ROS)
                *        $ rosservice call mavros/cmd/takeoff <tab>
                ****************************************************************

            Lets continue on how to publish:
                $ rostopic pub -r 10 /mavros/setpoint_position/global geographic_msgs/GeoPoseStamped <tab><tab>(for auto completion)

                $ rostopic pub -r 5 /mavros/<tab><tab>/<tab><tab> <tab><tab> <tab><tab>
            
            ** Services **  : just like subscriptions but with a return value
                $ rosservice call /mavros/cmd/land <tab><tab>

                To check the <service> info:
                    $ rosservice info <Service>
                    $ rosservice info /mavros/set_mode

                    An important aspect here is the <Type> of the service, then we can do:
                        $ rossrv info <Service type>
                        $ rossrv info mavros_msgs/SetMode


**Examples**

1. Move the vehicle arround in the surroundings (local position frame):
    pxh> commander takeoff
    pxh> commander mode offboard
    $ rostopic pub -r 5 /mavros/setpoint_position/local geometry_msgs/PoseStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
pose:
  position:
    x: 1.0
    y: 0.0
    z: 4.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 0.0" 