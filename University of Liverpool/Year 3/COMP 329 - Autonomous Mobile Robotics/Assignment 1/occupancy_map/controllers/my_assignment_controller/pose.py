# Pose Class Definition
# File: pose.py
# Date: 7th Jan 2022
# Description: Pose Class support for COMP329 Programming Assignment (2022)
# Author: Terry Payne (trp@liv.ac.uk)


# ==============================================================
# COMP329 2024 Programming Assignment
# ==============================================================
# 
# The aim of the assignment is to move the robot around the arena
# in such a way as to generate an occupancy grid map of the arena
# itself.  Full details can be found on CANVAS for COMP329
#
# This copy of the pose class is the same as that downloaded from
# COMP329 Lab Tutorial 6. It requires no further update, and can
# be used as is.
# ==============================================================

import math

class Pose:
    """ 
    A class to represent the pose of some object (robot, sensor, etc)
    
    ...
    
    Attributes
    ----------
    x : float
        x in local coordinate system
    y : float
        y in local coordinate system
    ˚theta : float
        heading in radians from the axis y=0, in the range -pi ... +pi 

    Methods
    -------
    set_position(x, y, theta):
        updates all the parameters of the pose instance

    """
    def __init__(self, x=0.0, y=0.0, new_theta=0.0):
        """
        Constructs all the necessary attributes for the pose object.

        Parameters
        ----------
        x : float
            x in local coordinate system
        y : float
            y in local coordinate system
        theta : float
            heading in radians from the axis y=0, in the range -pi ... +pi 
        """
        self.set_position(x, y, new_theta)

        
    @property
    def theta(self):
        return self._theta
        
    @theta.setter
    def theta(self, new_theta):
        self._theta = self.range_angle(new_theta)
        
    def range_angle(self, t):
        """ Ensure that angle t is in the range -\pi..\pi """
        if (t > math.pi):
            t = -(2 * math.pi) + t
        elif (t < -math.pi):
            t = (2 * math.pi) + t
        return t

    
    def set_position(self, x, y, new_theta):
        self.x = x
        self.y = y
        self.theta = new_theta

    def set_pose_position(self, p):
        """ Set the pose parameters given a pose object """
        self.x = p.x
        self.y = p.y
        self.theta = p.theta

    
    def get_dtheta(self, t):
        """ Find the difference in radians between some heading and the current pose """
        d = t - self.theta
        return self.range_angle(d)

    def get_range(self, target):
        """ Gets the bearing from the current pose to the location of a target pose """
        dx = target.x - self.x
        dy = target.y - self.y
        return math.sqrt(dx**2 + dy**2)

    def get_bearing(self, target):
        """ Gets the bearing from the current pose to the location of a target pose """
        dx = target.x - self.x
        dy = target.y - self.y
        return self.range_angle(math.atan2(dy, dx) - self.theta)      

    def __str__(self):
        return '({0:.2f}, {1:.2f}, {2:.2f})'.format(self.x, self.y, self._theta)
