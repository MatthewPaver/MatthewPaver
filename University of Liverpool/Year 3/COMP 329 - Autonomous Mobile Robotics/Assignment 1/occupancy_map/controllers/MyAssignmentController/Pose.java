// File: Pose.java
// Date: 30th Dec 2020
// Description: Pose Class support for COMP329 Programming Assignment (2020)
// Author: Terry Payne
// Modifications:
//     Addition of getDeltaTheta() and update to the toString() method - 26th Nov 2021
//     Update to Pose to include calculating range and bearing between two poses
/**
 * The Pose class for a robot 
 * Based on Worksheet 3 for COMP329, Nov 2020
 * 
 * @author Dr Terry R. Payne (trp@liv.ac.uk)
 *
 */
 
// ==============================================================
// COMP329 2024 Programming Assignment
// ==============================================================
// 
// The aim of the assignment is to move the robot around the arena
// in such a way as to generate an occupancy grid map of the arena
// itself.  Full details can be found on CANVAS for COMP329
//
// This copy of the pose class is the same as that downloaded from
// COMP329 Lab Tutorial 6. It requires no further update, and can
// be used as is.
// ==============================================================

 
public class Pose {
  private double x;    // position on x axis - assume units are meters
  private double y;    // position on y axis - assume units are meters
  private double theta;  // This determines the angle (radians) anticlockwise from the x-axis line

  // ==================================================================================
  // Constructors
  // ==================================================================================
  public Pose() {
    this(0.0,0.0,0.0);
  }

  public Pose(double xpos, double ypos, double theta) {
    this.x = xpos;
    this.y = ypos;
    this.setTheta(theta);
  }

  public Pose(Pose p) {
    this.x = p.getX();
    this.y = p.getY();
    this.setTheta(p.getTheta());
  }

  // ==================================================================================
  // Internal methods  
  // ==================================================================================
  private final double range_angle(double theta) {
    // Ensure that theta is in the range -\pi..\pi
    double result;
    if (theta>Math.PI) {
      result=theta-(2 * Math.PI);
    } else if (theta < -Math.PI) {
      result = (2 * Math.PI)+theta;
    } else {
      result = theta;
    }
    return result;
  }

  // ==================================================================================
  // Getters / Setters  
  // ==================================================================================
  // Note that the following method is defined as final, as it is used in the constructor
    
  public final void setTheta(double theta) {
    this.theta = this.range_angle(theta);
  }

  public void setPosition(double xpos, double ypos, double theta) {
    this.x = xpos;
    this.y = ypos;
    this.setTheta(theta);
  }

  public void setPosition(Pose p) {
    this.setPosition(p.getX(), p.getY(), p.getTheta());
  }

  public String toString() {
    return String.format("<%.03f", this.x) + ", " +
        String.format("%.03f", this.y) + ", " +
        String.format("%.03f", this.theta) +">";
  }

  public double getX() {
    return x;
  }

  public double getY() {
    return y;
  }

  public double getTheta() {
    return theta;
  }
    
  // Find the difference in radians between some heading and the current pose
  public double getDeltaTheta(double theta) {
    return this.range_angle(theta - this.theta);
  }
  
  // Gets the distance from the current pose to a target pose
  public double get_range(Pose target) {
    double dx = (target.x - this.x);
    double dy = (target.y - this.y);
    return Math.sqrt(Math.pow(dx,2)+Math.pow(dy,2));
  }

  // Gets the bearing from the current pose to the location of a target pose
  public double get_bearing(Pose target) {
    double dx = (target.x - this.x);
    double dy = (target.y - this.y);
    return this.range_angle(Math.atan2(dy, dx) - this.theta);    
  }

}