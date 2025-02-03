# pioneer_simpleproxsensors Class Definition
# File: pioneer_simpleproxsensors.py
# Date: 7th Nov 2024
# Description: Proximity Sensor support for COMP329 Lab Tutorials (2024)
# Author: Terry Payne (trp@liv.ac.uk)
# Modifications: Based on pioneer_proxsensors.py (24th Jan 2022) used for
#                COMP329 Programming Assignment (2022)

# ==============================================================
# COMP329 2024 Programming Assignment
# ==============================================================
# 
# The aim of the assignment is to move the robot around the arena
# in such a way as to generate an occupancy grid map of the arena
# itself.  Full details can be found on CANVAS for COMP329
#
# This copy of the PioneerSimpleProxSensors class is the same
# as that developed in COMP329 Lab Tutorial 5 (if you haven't
# completed that lab, then please read through the details to
# understand how this class works, but this is the final version).
# It requires no further update, and can be used as is.
# ==============================================================

import math
import pose

class PioneerSimpleProxSensors:
    """ A custom class to manage the 16 proximity sensors on a Pioneer Adept robot """

    MAX_NUM_SENSORS = 16

    def __init__(self, robot):
        
        self.robot = robot
        timestep = int(robot.getBasicTimeStep())

        ## enabling touch sensor 
        self.ts = robot.getDevice("touch sensor") 
        self.ts.enable(timestep)


        # Dimensions of the Robot
        # Note that the dimensions of the robot are not strictly circular, as 
        # according to the data sheet the length is 485mm, and width is 381mm
        # so we assume for now the aprox average of the two (i.e. 430mm), in meters
        self.radius = 0.215

        # Insert Constructor Code Here
        # ------------------------------------------
        # set up proximity detectors
        self.ps = []
        for i in range(self.MAX_NUM_SENSORS):
            sensor_name = 'so' + str(i)
            self.ps.append(robot.getDevice(sensor_name))
            self.ps[i].enable(timestep)
    

        # The following array determines the orientation of each sensor, based on the
        # details of the Pioneer Robot Stat sheet.  Note that the positions may be slightly
        # inaccurate as the pioneer is not perfectly round.  Also these values are in degrees
        # and so may require converting to radians.  Finally, we assume that the front of the
        # robot is between so3 and so4.  As the angle between these is 20 deg, we assume that 
        # they are 10 deg each from the robot heading         

        ps_degAngles = [
            90, 50, 30, 10, -10, -30, -50, -90,
            -90, -130, -150, -170, 170, 150, 130, 90
        ]
        ps_angles = [None] * len(ps_degAngles)
        for i in range(len(ps_angles)):
            ps_angles[i] = math.radians(ps_degAngles[i])
                
        # -------------------------------------------
        # Determine the poses of each of the sensors
        self.ps_pose = []
        for i in ps_angles:
            p = pose.Pose(math.cos(i) * self.radius, math.sin(i) * self.radius, i)
            self.ps_pose.append(p)

        # ------------------------------------------
        # Determine max range from lookup table
        lt = self.ps[0].getLookupTable()
        print(f"Lookup Table has {len(lt)} entries")
        self.max_range = 0.0
        for i in range(len(lt)):
            if ((i%3) == 0):
                self.max_range = lt[i]
            print(f" {lt[i]}", end='')
            if ((i%3) == 2):
                print("") # Newline

        self.max_value = self.ps[0].getMaxValue()
        print(f"Max Range: {self.max_range}")
        
    # ==================================================================================
    # External (Public) methods
    # ==================================================================================
  
    # Insert public methods here
    def get_maxRange(self):
        return self.max_range

    def get_number_of_sensors(self):
        return len(self.ps)

    def get_value(self, i):
        if (i < len(self.ps)):
            return self.max_range - (self.max_range/self.max_value * self.ps[i].getValue())
        else:
            print("Out of range error in get_value()")
            return None

    def get_rawvalue(self, i):
        if (i < len(self.ps)):
            return self.ps[i].getValue()
        else:
            print("Out of range error in get_rawvalue()")
            return None
            
    def get_relative_sensor_pose(self, i):
        if (i < len(self.ps)):
            p = self.ps_pose[i]
            return pose.Pose(p.x, p.y, p.theta)
        else:
            print("Out of range error in get_relative_sensor_pose()")
            return pose.Pose(0, 0, 0)

    # =====================================================  
    # New method used by the COMP329 Programming Assignment

    def get_radius(self):
        return self.radius
