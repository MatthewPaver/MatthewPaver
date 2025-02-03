// File: OccupancyGrid.java
// Date: 20 Nov 2021
// Description: OccupancyGrid Class support for COMP329 Programming Assignment (2021)
// Author: Terry Payne
// Modifications 2024:
//          Updated to include pose by the map method
//          Stores the arena value to check if it set set up, and returns if failure
/**
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
// This occupancy grid class constructs an array corresponding to the
// size of the arena and the number of cells specified in the constructor.
// This is done by looking for object ARENA from the scene tree.  It also
// checks the size of the display attached to the robot (as specified
// in the constructor arguments) and scales the resulting map onto the
// display.
//
// The constructor is called with the following arguments:
//  - an instance of a Supervisor robot object
//  - the number of cells per meter.  The higher the number, the higher
//    the resolution of the map.  I recommend between 5-20.
//  - the name of the display object on the robot where the map appears
//  - the initial pose of the robot
//  - an instance of the PioneerSimpleProxSensors object
//
// To update the occupancy grid, the map() method is called with the current Pose
// To draw the occupancy grid, the paint() method is called.
//
// If an ARENA object is not defined, then a warning message on the
// console will appear.  You should ensure that the DEF field of the
// Rectangle Arena is filled with this string "ARENA"
//
//
// THIS IS WHAT YOU NEED TO DO
// ===========================
// The one thing missing in this class is the code to generate the
// log-odds value for each cell, depending on whether it is occupied,
// free, or unknown (for this return lprior, which is defined below).
// This should be done in the method
//
//     private double invSensorModel(Pose p, double x, double y);
// 
// This method takes the position of the current pose, and the (x,y)
// location of a cell based on a real coordinate point (i.e. the
// same coordinate system as a pose).
// Currently the method returns the value of the variable logodds; a
// good approach would be to set this to be the appropriate value 
// for the cell.
// 
// The method is called at the end of the map() method, which
// iterates through every cell in the occupancy grid.
//
// Details of the inverse sensor model can be found in Part 3 of
// the lecture notes (pages 51-66).
//
//    COMP329 7 Occupancy Grids and Mapping with Known Poses 2024-25.pdf
// 
// There is no need to implement the more advanced sensor model, but some
// thought should be given as to the choice of values for the occupied and
// empty log odds values.  See the definition of 'lprior' below.
// ==============================================================



 
import com.cyberbotics.webots.controller.Supervisor;
import com.cyberbotics.webots.controller.DistanceSensor;
import com.cyberbotics.webots.controller.Display;
import com.cyberbotics.webots.controller.Node;
import com.cyberbotics.webots.controller.Field;

 
public class OccupancyGrid {
  // --------------------------------
  // Robot state variables  
  private Supervisor robot;     // Reference to the Robot itself
  private Pose robot_pose;       // track the pose of the robot in the global coordinate system
  private PioneerSimpleProxSensors prox_sensors;  // reference to the sensor object
  private double radius;        // radius of the robot (assume it is round)
  
  // --------------------------------
  // Display state variables  
  private Display display;      // reference to the display device on the robot
  private int device_width;     // width of the display device
  private int device_height;    // height of the display device
  private double scale_factor;  // Scale factor to scale rendered map to the maximal dimension on the display


  // --------------------------------
  // Occupancy Grid variables
  private Node arena;
  private double[] grid;         // Array of log odds elements
  private int num_row_cells;	    // number of cells across
  private int num_col_cells;	    // number of cells up
  private int cell_width;     // Width of a cell (wrt arena)
  private int cell_height;    // Height of a cell (wrt arena)
  private double arena_width;    // Width of the arena
  private double arena_height;   // Height of the arena
  private double coverage;       // normalised level of map coverage

  // Fixed log odds values (found empirically)  
  private final double lprior = Math.log(0.5/(1-0.5));

  // Constants for the inverse sensor model (values are halved to optimise performance)
  private final double HALFALPHA = 0.02;           // Thickness of any wall found
  private final double HALFBETA = Math.PI/36.0;    // sensor cone opening angle 


  // ==================================================================================
  // Constructor
  // ==================================================================================
  public OccupancyGrid(Supervisor r,
                       int grid_scale,
                       String display_name,
                       Pose p,
                       PioneerSimpleProxSensors prox_sensors) {
    this.robot = r;
    this.robot_pose = p;
    this.prox_sensors = prox_sensors;
    this.radius = prox_sensors.get_radius();

    // ---------------------------------------------------------------------------
    // Store Arena state instance variables
    this.arena = robot.getFromDef("ARENA");
    if (this.arena == null) {
      System.err.println("COMP329 >>>Please define the DEF parameter of the RectangleArena as ARENA in the scene tree.<<<");
      return;
    }
    Field floorSizeField = arena.getField("floorSize");
    double floorSize[] = floorSizeField.getSFVec2f();
    this.arena_width = floorSize[0];
    this.arena_height = floorSize[1];
    
    // ---------------------------------------------------------------------------
    // Initialise grid - grid_scale cells per m
    this.num_row_cells = (int) (grid_scale*arena_width);
    this.num_col_cells = (int) (grid_scale*arena_height);
    System.out.println(String.format("Buidling an Occupancy Grid Map of size %d x %d",
                       this.num_row_cells, this.num_col_cells));

    this.grid = new double[this.num_row_cells*this.num_col_cells];
    for (int i=0; i < this.grid.length; i++)
      this.grid[i] = lprior;    

     // ------------------------------------------
     // If provided, set up the display
    this.display = this.robot.getDisplay(display_name);
    if (this.display != null) {
      this.device_width = this.display.getWidth();
      this.device_height = this.display.getHeight();
      // Determine the rendering scale factor
      double wsf = ((double) this.device_width) / this.arena_width;
      double hsf = ((double) this.device_height) / this.arena_height;
      this.scale_factor = Math.min(wsf, hsf);   

      this.cell_width = this.device_width / this.num_row_cells;
      this.cell_height = this.device_height / this.num_col_cells;
    

    } else {
      this.device_width = 0;
      this.device_height = 0;
      this.scale_factor = 0.0;
    }
  }

  // ==================================================================================
  // Getters / Setters  
  // ================================================================================== 

  // The following can be used externally to check the status of 
  // the grid map, for example, to develop an exploration strategy.  
  public int get_num_row_cells() {
    return this.num_row_cells;
  }
  public int get_num_col_cells() {
    return this.num_col_cells;
  }
  public int get_grid_size() {
    return this.grid.length;
  }
  public double get_cell_probability(int index) {
    return cell_probability(grid[index]);
  }
 
  // ================================================================================== 
  public void set_pose(Pose p) {
    // Sets the pose of the robot.  If an instance of a pose has yet to be created, then create one
    // Always copy the pose value rather than retain the instance, to ensure it is not side effected
    this.robot_pose.setPosition(p.getX(), p.getY(), p.getTheta());
  }
  
  // Map the real coordinates to screen coordinates assuming
  // the origin is in the center and y axis is inverted
  private int scale(double l) {
    return (int) (this.scale_factor * l);
  }
  private int mapx(double x) {
    return (int) ((this.device_width/2.0) + this.scale(x));
  }
  private int mapy(double y) {
    return (int) ((this.device_height/2.0) - this.scale(y));
  }

  private double cell_probability(double lodds) {
    return 1-(1/(1+Math.exp(lodds)));
  }
    
  // ---------------------------------------------------------------------------
  // UPDATE WITH A FULLY WORKING SENSOR MODEL HERE
  // ---------------------------------------------------------------------------
  private double invSensorModel(Pose p, double x, double y) {
  
    // Takes the position of the current pose, and the (x,y) location of a cell
    // based on a real coordinate point (i.e. the same coordinate system as a pose)
    // Add code here to implement the inverse sensor model
    // Some initial code is provided to get the range, and bearing, and then
    // ensure that if the location is inside the robot, we set the range to zero
    
    // Determine the range and bearing of the cell
    double deltaX = x-p.getX();
    double deltaY = y-p.getY();
    double r = Math.sqrt(Math.pow(deltaX,2)+Math.pow(deltaY,2));     // range
    double phi = Math.atan2(deltaY, deltaX) - p.getTheta();          // bearing
    double logodds = lprior;                                         // default return value

    // Note that the above code assumes range based
    // on the robot and not the sensor position
    if (r>this.radius)
      r=r-this.radius;    // Remove the distance from the robot center to sensor
    else  
      r=0.0;              // If negative, then cell center is behind the sensor and
                          // within the robot radius.  So just reset to zero.

    // --------------------------------
    // INSERT SIMPLE SENSOR MODEL HERE
    //
    // Details of the inverse sensor model can be found in Part 3 of
    // the lecture notes (pages 51-66).
    //
    // COMP329 7 Occupancy Grids and Mapping with Known Poses 2024-25.pdf
    // 
    // --------------------------------


    return logodds;
  }

  // ==================================================================================
  // External Methods  
  // ==================================================================================
  // Update the occupancy grid based on the current pose

  public void map(Pose p) {
    
    if (this.arena == null) {
      System.err.println("COMP329 >>>Please define the DEF parameter of the RectangleArena as ARENA in the scene tree.<<<");
      return;
    }

    double x;                              // x coord
    double y;                              // y coord
    double x_orig_offset = this.arena_width/2.0;   // Offset for origin along x axis
    double y_orig_offset = this.arena_height/2.0;  // Offset for origin along y axis
    
    double x_inc = this.arena_width/this.num_row_cells;
    double y_inc = this.arena_height/this.num_col_cells;

    double x_cell_offset = x_inc/2.0;          // offset to center of cell along x axis
    double y_cell_offset = y_inc/2.0;          // offset to center of cell along y axis

    this.robot_pose.setPosition(p.getX(), p.getY(), p.getTheta());    
    
    for (int i=0; i < this.grid.length; i++) {
      // Convert cell into a coordinate.  Recall that the arena is dimensions -n..+n
      x = x_inc * (i%this.num_row_cells)-x_orig_offset+x_cell_offset;
      y = -(y_inc * (i/this.num_row_cells)-y_orig_offset+y_cell_offset);
      
      // Log Odds Update Function
      this.grid[i] = this.grid[i] + invSensorModel(this.robot_pose, x, y) - lprior;
    }
  } 
  
  // ==================================================================================
  // Update the display using a grayscale to represent the different probabilities
  // Note that a percentage of coverage is generated, based on counting the number of
  // cells have have a probability < 0.1 (empty) or > 0.9 (occupied)

  public void paint() { 
    if (this.arena == null) {
      System.err.println("COMP329 >>>Please define the DEF parameter of the RectangleArena as ARENA in the scene tree.<<<");
      return;
    }

    if (this.display==null)
      return;
    
    // draw a background
    this.display.setColor(0xF0F0F0);     // Off White
    this.display.fillRectangle(0, 0, this.device_width, this.device_height);
    
    double cellProb;          // probabilty of occuupancy for each cell
    this.coverage = 0.0;
    for (int i=0; i< this.grid.length; i++) {
      cellProb = this.cell_probability(this.grid[i]);
      int x = this.cell_width * (i%this.num_row_cells);
      int y = this.cell_height * (i/this.num_row_cells);
                
      // Determine colour - Uses a very simple approach for now with graduated grey shades
      if (cellProb < 0.1) this.display.setColor(0xFFFFFF);
      else if (cellProb < 0.2) this.display.setColor(0xDDDDDD);
      else if (cellProb < 0.3) this.display.setColor(0xBBBBBB);
      else if (cellProb < 0.4) this.display.setColor(0x999999);
      else if (cellProb > 0.9) this.display.setColor(0x000000);
      else if (cellProb > 0.8) this.display.setColor(0x222222);
      else if (cellProb > 0.7) this.display.setColor(0x444444);
      else if (cellProb > 0.6) this.display.setColor(0x666666);
      else this.display.setColor(0x787878);
      
      this.display.fillRectangle(x, y, this.cell_width, this.cell_height);
      
      if ((cellProb < 0.1) || (cellProb > 0.9))
        this.coverage += 1.0;
    }
    // normalise coverage
    this.coverage = this.coverage / this.grid.length;

    this.display.setColor(0x3C3C3C);     // Dark Grey
    // Draw Vertical Lines
    for (int i=0, x=0; i <= this.num_row_cells; i++, x+= this.cell_width) {    // Draw extra border after last cell
      this.display.drawLine(x, 0, x, this.device_height);
    }           
      
    // Draw Horizontal Lines
     for (int i=0, y=0; i <= this.num_row_cells; i++, y+= this.cell_height) {    // Draw extra border after last cell
      this.display.drawLine(0, y, this.device_width, y);
    }           

    // Draw Robot Body          
    this.display.setColor(0xFFFFFF);     // White
    this.display.fillOval(this.mapx(this.robot_pose.getX()),
                          this.mapy(this.robot_pose.getY()),
                          this.scale(this.radius),
                          this.scale(this.radius));    
    
    this.display.setColor(0x3C3C3C);     // Dark Grey
    this.display.drawOval(this.mapx(this.robot_pose.getX()),
                          this.mapy(this.robot_pose.getY()),
                          this.scale(this.radius),
                          this.scale(this.radius));    
    // Need to indicate heading          
    this.display.drawLine(this.mapx(this.robot_pose.getX()),
                          this.mapy(this.robot_pose.getY()),
                          this.mapx(this.robot_pose.getX() + Math.cos(this.robot_pose.getTheta()) * this.radius),
                          this.mapy(this.robot_pose.getY() + Math.sin(this.robot_pose.getTheta()) * this.radius));
                           
    // Provide coverage percentage
    this.display.setColor(0xF0F0F0);     // Off White
    this.display.fillRectangle(this.device_width-80, this.device_height-18, this.device_width-20, this.device_height);
    this.display.setColor(0x000000);     // Black
    this.display.drawRectangle(this.device_width-80, this.device_height-18, this.device_width-20, this.device_height);


    this.display.setFont("Arial", 10, true);  // font size = 10, with antialiasing
    this.display.drawText(String.format("%.2f%%", this.coverage * 100), this.device_width-60,this.device_height-14);
  
  } 
}