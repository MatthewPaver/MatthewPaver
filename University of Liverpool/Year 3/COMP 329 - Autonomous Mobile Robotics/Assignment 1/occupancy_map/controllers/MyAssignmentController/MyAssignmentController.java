// File:          MyAssignmentController.java
// Date:
// Description:
// Author:
// Modifications:

// ==============================================================
// COMP329 2024 Programming Assignment
// ==============================================================
// 
// The aim of the assignment is to move the robot around the arena
// in such a way as to generate an occupancy grid map of the arena
// itself.  Full details can be found on CANVAS for COMP329
//
// This controller file simply creates a controller and initialises
// the occupancy grid class.  You will need to complete the code in
// the occupancy grid class to implement the inverse sensor model
// and complete the update method.
//
// Note that the size of the occupancy grid can be changed (see below)
// as well as the update frequency of the map, and whether or not a
// map is generated. Changing these values may be useful during the
// debugging phase, but ensure that the solution you submit generates
// an occupancy grid map of size 100x100 cells.
//
// Note that this class makes the following assumptions:
//
//	PioneerCLNav
//	============
//	You have a navigator class called PioneerCLNav that implements
//      the following methods (based on Lab Tutorial 6):
//	  - a constructor that takes two arguments, an instance of a Supervisor
//	    robot object and an instance of a PioneerSimpleProxSensors
//	  - set_goal() which defines a destination pose
//	  - update() that makes any changes necessary as part of navigation
//	You can replace these with other calls if you want to use a different
//	class or means of navigation.  Note this is NOT included.
//	Note - if you use a different class you must implement a method called
//	get_real_pose() that returns an object of type Pose representing the true
//	location of the robot.  Examples of this class are used in Lab Tutorials 3 and 6.
//
//	PioneerSimpleProxSensors
//	========================
//	You have a sensor class based on the work in Lab 5.  This is used by
//	navigator class, but could also be used by a navigator class.  Code
//	for the version used in the tutorial is included with the assignment.
//
//	Pose
//	====
//	This is the latest version of the Pose class (it includes some additional
//	methods used in Lab Tutorial 6), and is used throughout the COMP329
//	code base.  A version is included with the assignment.
//
//	OccupancyGrid
//	=============
//	You have an occupancy grid class.  The constructor takes the following
//	arguments:
//	  - an instance of a Supervisor robot object
//	  - the number of cells per meter.  The higher the number, the higher
//	    the resolution of the map.  I recommend between 5-20.
//	  - the name of the display object on the robot where the map appears
//	  - the initial pose of the robot
//	  - an instance of the PioneerSimpleProxSensors object
//
//	To update the occupancy grid, call the map() method with the current Pose
//	To draw the occupancy grid, call the paint() method
//
//
// ==============================================================

import com.cyberbotics.webots.controller.Supervisor;

public class MyAssignmentController {


  // ==================================================================================
  // Main Methods 
  // ==================================================================================  
  public static void main(String[] args) {

    // ---------------------------------------------------------------------------
    // create the Supervised Robot instance.
    // ---------------------------------------------------------------------------
    Supervisor robot = new Supervisor();

    // get the time step of the current world.
    int timeStep = (int) Math.round(robot.getBasicTimeStep());

    // ---------------------------------------------------------------------------
    // initialise other classes such as the proximity and occupancy grid classes
    // ---------------------------------------------------------------------------
    PioneerSimpleProxSensors pps = new PioneerSimpleProxSensors(robot);
    PioneerCLNav nav = new PioneerCLNav(robot, pps);

    // 2nd argument determines how many cells per meter of the arena.
    // Use 10 for testing navigation, but 20 for high-quality map (slow)
    OccupancyGrid ogrid = new OccupancyGrid(robot, 10, "display", nav.get_real_pose(), pps);
    
    // ---------------------------------------------------------------------------
    // Initialise your exploration approach.  Here we just set an initial
    // way point as the goal.
    // INSERT INITIALISATION CODE HERE

    nav.set_goal(new Pose(0,-4,0));

    // ---------------------------------------------------------------------------
    // Main loop:
    while (robot.step(timeStep) != -1) {


      // ---------------------------------------------------------------------------
      // Add code to manage the movement or navigation here.  Remember not to write
      // blocking code, as the robot should loop here and update the map every cycle
      // INSERT NAVIGATION CODE HERE
     
      if (nav.update())
          break;

      // ----------------------------------------------------------------------------
      // the following two lines update the occupancy grid, and then display the grid
      // Comment out the method paint() if you don't want to see the occupancy grid

      ogrid.map(nav.get_real_pose());
      ogrid.paint();

      // ----------------------------------------------------------------------------
      
    };
    
    nav.update(); // ensures motors come to a stop

    // Enter here exit cleanup code.
  }
}
