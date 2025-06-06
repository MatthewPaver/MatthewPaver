# OccupancyGrid Class Definition
# File: occupancy_grid.py
# Date: 30th Jan 2022
# Description: Occupancy Grid in Python for COMP329 (2022)
# Author: Terry Payne (trp@liv.ac.uk)
#
#          Updated to include pose by the map method
#          Stores the arena value to check if it set set up, and returns if failure

# ==============================================================
# COMP329 2024 Programming Assignment
# ==============================================================
# 
# The aim of the assignment is to move the robot around the arena
# in such a way as to generate an occupancy grid map of the arena
# itself.  Full details can be found on CANVAS for COMP329
#
# This occupancy grid class constructs an array corresponding to the
# size of the arena and the number of cells specified in the constructor.
# This is done by looking for object ARENA from the scene tree.  It also
# checks the size of the display attached to the robot (as specified
# in the constructor arguments) and scales the resulting map onto the
# display.
#
# The constructor is called with the following arguments:
#  - an instance of a Supervisor robot object
#  - the number of cells per meter.  The higher the number, the higher
#    the resolution of the map.  I recommend between 5-20.
#  - the name of the display object on the robot where the map appears
#  - the initial pose of the robot
#  - an instance of the PioneerSimpleProxSensors object
#
# To update the occupancy grid, the map() method is called with the current Pose
# To draw the occupancy grid, the paint() method is called.
#
# If an ARENA object is not defined, then a warning message on the
# console will appear.  You should ensure that the DEF field of the
# Rectangle Arena is filled with this string "ARENA"
#
#
# THIS IS WHAT YOU NEED TO DO
# ===========================
# The one thing missing in this class is the code to generate the
# log-odds value for each cell, depending on whether it is occupied,
# free, or unknown (for this return lprior, which is defined below).
# This should be done in the method
#
#     private double invSensorModel(Pose p, double x, double y);
# 
# This method takes the position of the current pose, and the (x,y)
# location of a cell based on a real coordinate point (i.e. the
# same coordinate system as a pose).
# Currently the method returns the value of the variable logodds; a
# good approach would be to set this to be the appropriate value 
# for the cell.
# 
# The method is called at the end of the map() method, which
# iterates through every cell in the occupancy grid.
#
# Details of the inverse sensor model can be found in Part 3 of
# the lecture notes (pages 51-66).
#
#    COMP329 7 Occupancy Grids and Mapping with Known Poses 2024-25.pdf
# 
# There is no need to implement the more advanced sensor model, but some
# thought should be given as to the choice of values for the occupied and
# empty log odds values.  See the definition of 'lprior' below.
# ==============================================================

import sys
import math
import pioneer_simpleproxsensors as psps

import pose


class OccupancyGrid:
    """ A custom class to model an occupancy grid with optional display """

    # --------------------------------
    # define the display constants
    DARKGRAY = 0x3C3C3C
    GRAY = 0xABABAB
    BLACK = 0x000000
    WHITE = 0xFFFFFF
        
    # --------------------------------
    # Fixed log odds values (found empirically)  
    lprior = math.log(0.5/(1-0.5)) #Unknown
    locc = math.log(0.95/(1-0.95)) #occupied
    lfree = math.log(0.45/(1-0.45)) #Empty
    # Constants for the inverse sensor model (values are halved to optimise performance)

    HALFALPHA = 0.04            # Thickness of wall found
    HALFBETA = math.pi/36.0          # sensor cone opening angle 
    coverage = 0


    # ==================================================================================
    # Constructor
    # ==================================================================================

    def __init__(self, robot, grid_scale, display_name, robot_pose, prox_sensors):
        """
        Initialize the occupancy grid.

        Args:
            robot: Supervisor instance controlling the robot.
            grid_scale: Resolution of the grid in cells per meter.
            display_name: Name of the display device.
            robot_pose: Initial pose of the robot.
            prox_sensors: Instance of PioneerSimpleProxSensors for sensor data.
        """
        self.robot = robot
        self.robot_pose = robot_pose
        self.prox_sensors = prox_sensors
        self.radius = self.prox_sensors.get_radius()
        
        # Store Arena state instance variables
        self.arena = robot.getFromDef("ARENA")
        if self.arena is None:
            print("COMP329 >>>Please define the DEF parameter of the RectangleArena as ARENA in the scene tree.<<<", file=sys.stderr)
            return
            
           
        floorSize_field = self.arena.getField("floorSize")
        floorSize = floorSize_field.getSFVec2f()
        self.arena_width = floorSize[0]
        self.arena_height = floorSize[1]

        # ---------------------------------------------------------------------------
        # Initialise grid - grid_scale cells per m
        self.num_row_cells = int(grid_scale * self.arena_width)
        self.num_col_cells = int(grid_scale * self.arena_height)
        print(f"Buidling an Occupancy Grid Map of size {self.num_row_cells} x {self.num_col_cells}")

        self.grid = [self.lprior]*(self.num_row_cells * self.num_col_cells)
            
        # ------------------------------------------
        # If provided, set up the display
        self.display = robot.getDevice(display_name)
        if self.display is not None:
            self.device_width = self.display.getWidth()
            self.device_height = self.display.getHeight()
            
            #Determine the rendering scale factor           
            wsf = self.device_width / self.arena_width
            hsf = self.device_height / self.arena_height
            self.scalefactor = min(wsf, hsf)
            
            self.cell_width = int(self.device_width / self.num_row_cells)
            self.cell_height = int(self.device_height / self.num_col_cells)
        else:
            self.device_width = 0
            self.device_height = 0
            self.scalefactor = 0.0

    # ================================================================================== 
    # Getters / Setters
    # ================================================================================== 
    # The following can be used externally to check the status of the grid map,
    # for example, to develop an exploration strategy.  
    def get_num_row_cells(self):
        return self.num_row_cells    
    def get_num_col_cells(self):
        return self.num_col_cells
    # UPDATE - Corrected error in arguments for get_grid_size
    def get_grid_size(self):
        return len(self.grid)
    # UPDATE - call to cell_probability not scoped with "self"
    def get_cell_probability(self, i):
        return self.cell_probability(self.grid[i])

    def get_cell_probability_at_pose(self, p):
        # determine the cell at pose p
        x_inc = self.arena_width / self.num_row_cells
        y_inc = self.arena_height / self.num_col_cells

        col = int((p.x + self.arena_width / 2) / x_inc)
        row = int((-p.y + self.arena_height / 2) / y_inc)

        if col < 0 or col >= self.num_row_cells or row < 0 or row >= self.num_col_cells:
            return None

        i = row * self.num_row_cells + col
        return self.cell_probability(self.grid[i])

    # ================================================================================== 
    # helper methods for mapping to the display
    # Map the real coordinates to screen coordinates assuming
    #   the origin is in the center and y axis is inverted

    def scale(self, l):
        return int(l * self.scalefactor)
    def mapx(self, x):
        return int((self.device_width / 2.0) + self.scale(x))
    def mapy(self, y):
        return int((self.device_height / 2.0) - self.scale(y))

    def set_pose(self, p):
        self.robot_pose.set_pose_position(p)
        
    #Convert log odds into a probability
    #Update - handle overflow
    def cell_probability(self, lodds):
        # Handle overflow properly
        try:
            exp = math.exp(lodds)
        except:
            exp = math.inf
        return 1 - (1 / (1 + exp))
        

    # ---------------------------------------------------------------------------
    # UPDATE WITH A FULLY WORKING SENSOR MODEL HERE
    # ---------------------------------------------------------------------------  
    # Get log odds value for cell x,y given the current pose
    def inv_sensor_model(self, p, x, y):
        """
        Calculate the log-odds value for a cell at (x, y) using the inverse sensor model.

        Args:
            p: Current pose of the robot.
            x: X-coordinate of the cell.
            y: Y-coordinate of the cell.

        Returns:
            Log-odds value for the cell.
        """

        # ---------------------------------------------------------------------------
        # Determine the range and bearing of the cell
        deltaX = x - p.x
        deltaY = y - p.y
        r = math.sqrt(deltaX**2 + deltaY**2)  # Range to cell
        phi = math.atan2(deltaY, deltaX) - p.theta  # Bearing to cell
        logodds = self.lprior  # Default return value (unknown)

        # Adjust range based on the robot's radius
        if r > self.radius:
            r -= self.radius  # Remove the distance from the robot center to sensor
        else:
            r = 0.0  # If within the robot's radius, reset to zeroF

        # ---------------------------------------------------------------------------
        # Find the nearest sensor to the cell
        k = 0  # Sensor index
        kMinDelta = math.pi  # Smallest angular difference
        for j in range(self.prox_sensors.get_number_of_sensors()):
            sensor_pose = self.prox_sensors.get_relative_sensor_pose(j)
            kDelta = abs(sensor_pose.theta - phi)  # Angular difference
            if kDelta < kMinDelta:
                k = j
                kMinDelta = kDelta

        # ---------------------------------------------------------------------------
        # Determine which region the cell is in
        z = self.prox_sensors.get_value(k)  # Sensor reading
        if z == self.prox_sensors.get_maxRange():
            # Region 3 - Unknown
            logodds = self.lprior
        elif (r > min(self.prox_sensors.get_maxRange(), z + self.HALFALPHA)) or (kMinDelta > self.HALFBETA):
            # Region 3 - Unknown
            logodds = self.lprior
        elif (z < self.prox_sensors.get_maxRange()) and (r + self.HALFALPHA/2 >= z ):
            # Region 1 - Occupied
            logodds = self.locc
        elif r <= z:
            # Region 2 - Free
            logodds = self.lfree
  
        return logodds
            
	
	# Details of the inverse sensor model can be found in Part 3 of
	# the lecture notes (pages 51-66).
	#
	# COMP329 7 Occupancy Grids and Mapping with Known Poses 2024-25.pdf
	# 
	# --------------------------------




    # ==================================================================================
    # External Methods  
    # ==================================================================================
    # Update the occupancy grid based on the current pose

    def map(self, p):
        """
        Update the occupancy grid based on the robot's current position and sensor data.

        Args:
            p: Current pose of the robot.
        """
        if self.arena is None:
            print("COMP329 >>>Please define the DEF parameter of the RectangleArena as ARENA in the scene tree.<<<", file=sys.stderr)
            return

        x_orig_offset = self.arena_width / 2
        y_orig_offset = self.arena_height / 2

        x_inc = self.arena_width / self.num_row_cells
        y_inc = self.arena_height / self.num_col_cells

        x_cell_offset = x_inc / 2
        y_cell_offset = y_inc / 2
        self.robot_pose.set_pose_position(p)

        radius_threshold = self.HALFALPHA*4  # Occupancy radius in meters

        # Step 1: Update cells using the robots current occupied cells because its obviously empty
        for row in range(self.num_col_cells):
            for col in range(self.num_row_cells):
                # Calculate the real-world position of the cell
                x = x_inc * col - x_orig_offset + x_cell_offset
                y = -(y_inc * row - y_orig_offset + y_cell_offset)

                # Calculate distance from the robot's position
                distance = ((x - self.robot_pose.x) ** 2 + (y - self.robot_pose.y) ** 2) ** 0.5
                if distance <= 0.08:
                    grid_index = row * self.num_row_cells + col
                    self.grid[grid_index] = -4 #Setting to completely empty
            
        # Step 2: Update cells using the inverse sensor model
        for i in range(len(self.grid)):
            x = x_inc * int(i % self.num_row_cells) - x_orig_offset + x_cell_offset
            y = -(y_inc * int(i / self.num_row_cells) - y_orig_offset + y_cell_offset)

            self.grid[i] = self.grid[i] + self.inv_sensor_model(self.robot_pose, x, y) - self.lprior
        
        # Step 3: Propagate occupied status to unknown cells only to auto complete
        new_grid = self.grid.copy()
        if self.get_coverage() >95: # Waiting the coverage to be above 95% to start
            for row in range(self.num_col_cells):
                for col in range(self.num_row_cells):
                    index = row * self.num_row_cells + col
                    if abs(self.grid[index] - self.lprior) > 0.01:
                        # Skip known cells (either free or occupied)
                        continue

                    # Check neighbors within 0.4m radius
                    occupied_neighbors = 0
                    total_neighbors = 0

                    for r in range(self.num_col_cells):
                        for c in range(self.num_row_cells):
                            neighbor_index = r * self.num_row_cells + c
                            if neighbor_index == index:
                                continue  # Skip the cell itself

                            # Convert indices to real-world coordinates
                            x1 = x_inc * c - x_orig_offset + x_cell_offset
                            y1 = -(y_inc * r - y_orig_offset + y_cell_offset)
                            x2 = x_inc * col - x_orig_offset + x_cell_offset
                            y2 = -(y_inc * row - y_orig_offset + y_cell_offset)

                            # Calculate distance between the two cells
                            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                            if distance <= radius_threshold:
                                total_neighbors += 1
                                if self.cell_probability(self.grid[neighbor_index]) > 0.9:
                                    occupied_neighbors += 1

                    # If a majority of neighbors within 0.4m are occupied, mark this cell as occupied
                    if total_neighbors > 0 and occupied_neighbors / total_neighbors >= 0.5:  # 50% threshold
                      
                        new_grid[index] = self.locc

        # Update the grid with the new values
        self.grid = new_grid

    # ==================================================================================
    # Update the display using a grayscale to represent the different probabilities
    # Note that a percentage of coverage is generated, based on counting the number of
    # cells have have a probability < 0.1 (empty) or > 0.9 (occupied)

    def paint(self):

        if self.arena is None:
            print("COMP329 >>>Please define the DEF parameter of the RectangleArena as ARENA in the scene tree.<<<", file=sys.stderr)
            return

        if self.display is None:
            return

        # draw a backgound
        self.display.setColor(0xF0F0F0)
        self.display.fillRectangle(0, 0, self.device_width, self.device_height)
        
        # draw values for occupancy grid  
        self.coverage = 0.0  
        for i in range(len(self.grid)):
            p = self.cell_probability(self.grid[i])
            x = self.cell_width * int(i % self.num_row_cells)
            y = self.cell_height * int(i / self.num_col_cells)
                        
            if (p < 0.1):
                self.display.setColor(self.WHITE)
            elif (p < 0.2):
                self.display.setColor(0xDDDDDD)
            elif (p < 0.3):
                self.display.setColor(0xBBBBBB)
            elif (p < 0.4):
                self.display.setColor(0x999999)
            elif (p > 0.9):
                self.display.setColor(self.BLACK)
            elif (p > 0.8):
                self.display.setColor(0x222222)
            elif (p > 0.7):
                self.display.setColor(0x444444)
            elif (p > 0.6):
                self.display.setColor(0x666666)
            else:
                self.display.setColor(self.GRAY)
                
            self.display.fillRectangle(x, y, self.cell_width, self.cell_height)
            
            if(p < 0.1) or (p > 0.9):
                self.coverage += 1.0
        
        # normalise coverage
        self.coverage = self.coverage / len(self.grid)
        
        self.display.setColor(self.GRAY)
        # vertical lines
        x=0
        for i in range(self.num_row_cells):
            self.display.drawLine(x, 0, x, self.device_height)
            x += self.cell_width

        # horizontal lines
        y=0
        for j in range(self.num_row_cells):
            self.display.drawLine(0, y, self.device_height, y)
            y += self.cell_height
                
        # draw robot body
        self.display.setColor(self.WHITE)
        self.display.fillOval(self.mapx(self.robot_pose.x),
                              self.mapy(self.robot_pose.y),
                              self.scale(self.radius),
                              self.scale(self.radius))
                              
        self.display.setColor(self.DARKGRAY)
        self.display.drawOval(self.mapx(self.robot_pose.x),
                              self.mapy(self.robot_pose.y),
                              self.scale(self.radius),
                              self.scale(self.radius))
        self.display.drawLine(self.mapx(self.robot_pose.x),
                              self.mapy(self.robot_pose.y),
                              self.mapx(self.robot_pose.x + math.cos(self.robot_pose.theta) * self.radius),
                              self.mapy(self.robot_pose.y + math.sin(self.robot_pose.theta) * self.radius))                             
        
        # Provide coverage percentage
        self.display.setColor(0xF0F0F0)  # Off White
        self.display.fillRectangle(self.device_width-80, self.device_height-18, self.device_width-20, self.device_height)
        self.display.setColor(0x000000)  # Black
        self.display.drawRectangle(self.device_width-80, self.device_height-18, self.device_width-20, self.device_height)


        self.display.setFont("Arial", 10, True)
        self.display.drawText(f"{self.coverage * 100:.2f}%", self.device_width-60, self.device_height-14);

    def get_coverage(self):
        """Get the current coverage percentage."""
        return self.coverage * 100  # Return as percentage
