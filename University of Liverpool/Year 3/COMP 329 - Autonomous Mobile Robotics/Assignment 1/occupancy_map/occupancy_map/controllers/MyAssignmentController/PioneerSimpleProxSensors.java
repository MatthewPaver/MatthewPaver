// File: PioneerSimpleProxSensors.java
// Date: 7th Nov 2024
// Description: Represent the local area of the adept robot given its sonar sensors
// Author: Terry Payne
// Modifications:
//    * Based on PioneerProxSensors1.java which was developed on 28th Oct 2021 and then 
//      updated for the Programming Assignment 2021 (29th Nov 20201)
//    * Builds upon the Python version (pioneer_proxsensors.py - 24th Jan 2022)
//      that integrates the Pioneer sensors into the view for cleaner code
//

// ==============================================================
// COMP329 2024 Programming Assignment
// ==============================================================
// 
// The aim of the assignment is to move the robot around the arena
// in such a way as to generate an occupancy grid map of the arena
// itself.  Full details can be found on CANVAS for COMP329
//
// This copy of the PioneerSimpleProxSensors class is the same
// as that developed in COMP329 Lab Tutorial 5 (if you haven't
// completed that lab, then please read through the details to
// understand how this class works, but this is the final version).
// It requires no further update, and can be used as is.
// ==============================================================


import com.cyberbotics.webots.controller.DistanceSensor;
import com.cyberbotics.webots.controller.Robot;

public class PioneerSimpleProxSensors {
  // --------------------------------
  // Robot state variables  
  private Robot robot;          // Reference to the Robot itself
  private double radius;        // Radius of the robot body (for positioning sensors)
  
  // --------------------------------
  // Distance Sensor state variables  
  private DistanceSensor[] ps;  // array of distance sensors attached to the robot
  private double maxRange;      // we'll get this from the lookup table of so0
  private double maxValue;      // we'll get this from the parameters of so0

  private Pose[] psPose;        // the pose of each sensor (assuming the robot is a round cylinder)
  
  private final static int MAX_NUM_SENSORS = 16;            // Number of sensors on the robot

  // ==================================================================================
  // Constructors
  // ==================================================================================
  public PioneerSimpleProxSensors(Robot r) {
    this.robot = r;      
    
    // get the time step of the current world.
    int timeStep = (int) Math.round(this.robot.getBasicTimeStep());    

    // Note that the dimensions of the robot are not strictly circular, as 
    // according to the data sheet the length is 485mm, and width is 381mm
    // so we assume for now the aprox average of the two (i.e. 430mm), in meters
    this.radius = 0.215;         // in meters
  
    // Insert Constructor Code Here

    //------------------------------------------
    // set up proximity detectors
    ps = new DistanceSensor[MAX_NUM_SENSORS];

    for (int i = 0; i < MAX_NUM_SENSORS; i++) {
      String sensorName = "so" + i;
      this.ps[i] = robot.getDistanceSensor(sensorName);
      this.ps[i].enable(timeStep);
    }
    
    // The following array determines the orientation of each sensor, based on the
    // details of the Pioneer Robot Stat sheet.  Note that the positions may be slightly
    // inaccurate as the pioneer is not perfectly round.  Also these values are in degrees
    // and so may require converting to radians.  Finally, we assume that the front of the
    // robot is between so3 and so4.  As the angle between these is 20 deg, we assume that 
    // they are 10 deg each from the robot heading
    double[] psAngleDeg = { 90, 50, 30, 10, -10, -30, -50, -90,
                            -90, -130, -150, -170, 170, 150, 130, 90};

    double[] psAngles = new double[MAX_NUM_SENSORS];
    
    //------------------------------------------
    // Determine the pose (relative to the robot) of each of the sensors
    this.psPose = new Pose[psAngleDeg.length];    // Allocate the pose array
    for (int i=0; i< psAngleDeg.length; i++) {
      double theta = Math.toRadians(psAngleDeg[i]);
      this.psPose[i] = new Pose(Math.cos(theta)*this.radius,
                                Math.sin(theta)*this.radius,
                                theta);      
    }    

    //------------------------------------------
    // determine max range from lookup table  
    double[] lt = ps[0].getLookupTable();
    System.out.println("Lookup Table has "+lt.length+" entries");
    this.maxRange=0.0;
    for (int i=0; i< lt.length; i++) {
      if ((i%3)==0) this.maxRange=lt[i];
      System.out.print(" "+lt[i]+",");
      if ((i%3)==2) System.out.println("\n");
    }
    this.maxValue=ps[0].getMaxValue();
    System.out.println("Max Range: "+this.maxRange);
  }
    
  // ==================================================================================
  // External (Public) methods
  // ==================================================================================  
      
  // Insert public methods here
  public double get_maxRange() {
    return maxRange;
  }
  
  public int get_number_of_sensors() {
    return MAX_NUM_SENSORS;
  }
  
  public double get_value(int sensorID) {
    if (sensorID < MAX_NUM_SENSORS)
      return this.maxRange - (this.maxRange/this.maxValue * this.ps[sensorID].getValue());
    else
      System.err.println("Out of range error in get_value()");
    return this.maxRange;
  } 
  public double get_rawvalue(int sensorID) {
    if (sensorID < MAX_NUM_SENSORS)
      return this.ps[sensorID].getValue();
    else
      System.err.println("Out of range error in get_rawvalue()");
    return this.maxRange;
  }
 
  public Pose get_relative_sensor_pose(int sensorID) {
    if (sensorID < MAX_NUM_SENSORS)
      return new Pose(this.psPose[sensorID]);
    else
      System.err.println("Out of range error in get_relative_sensor_pose()");
    return new Pose();
  }
  
  // =====================================================  
  // New method used by the COMP329 Programming Assignment
  public double get_radius() {
    return this.radius;
  }

}