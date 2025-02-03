# PioneerNavigation Class Definition
# File: pioneer_nav1.py
# Date: 18th Oct 2022
# Description: Simple Navigation Class support (2022)
# Author: Terry Payne (trp@liv.ac.uk)

from controller import Supervisor
import math
import pose
from enum import Enum

class MoveState(Enum):
    STOP = 0
    FORWARD = 1
    ARC = 2
    CONFIGURE = 3

class PioneerNavigation:
    """ A custom class to initialise and manage simple navigation on a Pioneer Adept robot """

    WHEEL_RADIUS = 0.0975   # in meters
    AXEL_LENGTH = 0.31      # in meters

    def __init__(self, robot):
        self.robot = robot                        # reference to the robot
        self.robot_node = self.robot.getSelf()    # reference to the robot node
        self.robot_pose = self.get_real_pose()    # the robot's believed pose, based on real location
        self.state = MoveState.STOP               # initial state
        self.configure_str = "Configuring..."
        
        # Enable motors
        self.left_motor = self.robot.getDevice('left wheel')
        self.right_motor = self.robot.getDevice('right wheel')
        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))
        
        # Initialise motor velocity
        self.left_motor.setVelocity(0.0)
        self.right_motor.setVelocity(0.0)

    def get_real_pose(self):
        """ Get the actual position and orientation of the robot from the supervisor. """
        if self.robot_node is None:
            return pose.Pose(0, 0, 0)
            
        real_pos = self.robot_node.getPosition()
        rot = self.robot_node.getOrientation()
        theta = math.atan2(-rot[0], rot[3])
        return pose.Pose(real_pos[0], real_pos[1], theta)

    def configure_initialise_parameters(self, icr_omega):
        """ Initialise parameters to start the configuration process. """
        self.state = MoveState.CONFIGURE
        self.configure_str = "Configuring with omega = {}".format(icr_omega)
        
        # Set initial values for configuration parameters
        self.config_max_x = self.robot_pose.x
        self.config_min_x = self.robot_pose.x
        self.config_timer = 0
        self.config_omega = icr_omega

        # Set wheel speeds for rotation
        self.left_motor.setVelocity(0.0)
        self.right_motor.setVelocity(self.config_omega)

    def configure_check_parameters(self, timestep):
        """ Perform configuration and check parameters for one loop cycle. """
        # Update pose
        current_pose = self.get_real_pose()
        
        # Track min and max x positions
        self.config_max_x = max(self.config_max_x, current_pose.x)
        self.config_min_x = min(self.config_min_x, current_pose.x)
        
        # Increment timer
        self.config_timer += timestep

        # If the robot has completed a rotation, calculate and finish configuration
        if abs(current_pose.theta) < 0.01 and self.config_timer > 1000:  # Example condition
            axel_length = self.config_max_x - self.config_min_x
            self.configure_str = "Axel Length: {:.3f}m".format(axel_length)
            
            # Transition to STOP state after configuration
            self.state = MoveState.STOP
            self.stop()
        return self.configure_str

    def forward(self, target_dist, robot_linearvelocity):
        """ Move the robot forward for a specified distance. """
        wheel_av = (robot_linearvelocity / self.WHEEL_RADIUS)
        target_time = abs(target_dist / robot_linearvelocity)
        
        self.left_motor.setVelocity(wheel_av)
        self.right_motor.setVelocity(wheel_av)
        self.state = MoveState.FORWARD
        
        # Return target time as milliseconds
        return 1000.0 * target_time

    def arc(self, icr_angle, icr_r, icr_omega):
        """ Move the robot along an arc with specified parameters. """
        target_time = abs(icr_angle / icr_omega)

        if icr_angle < 0 and icr_omega > 0:
            print("Warning: negative angle with positive omega. Correcting omega direction.")
            icr_omega = -icr_omega

        # Calculate linear velocities for each wheel around ICR
        vl = icr_omega * (icr_r - (self.AXEL_LENGTH / 2))
        vr = icr_omega * (icr_r + (self.AXEL_LENGTH / 2))
        
        leftwheel_av = (vl / self.WHEEL_RADIUS)
        rightwheel_av = (vr / self.WHEEL_RADIUS)
        
        self.left_motor.setVelocity(leftwheel_av)
        self.right_motor.setVelocity(rightwheel_av)
        self.state = MoveState.ARC

        # Return target time as milliseconds
        return 1000.0 * target_time

    def stop(self):
        """ Stop the robot by setting both wheel velocities to zero. """
        self.left_motor.setVelocity(0.0)
        self.right_motor.setVelocity(0.0)
        self.state = MoveState.STOP
