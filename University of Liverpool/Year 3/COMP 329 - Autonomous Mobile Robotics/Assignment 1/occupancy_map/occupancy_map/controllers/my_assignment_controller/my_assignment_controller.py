"""my_assignment_controller controller."""

# ==============================================================
# COMP329 2024 Programming Assignment
# ==============================================================
# 
# The aim of the assignment is to move the robot around the arena
# in such a way as to generate an occupancy grid map of the arena
# itself.  Full details can be found on CANVAS for COMP329
#
# This controller file simply creates a controller and initialises
# the occupancy grid class.  You will need to complete the code in
# the occupancy grid class to implement the inverse sensor model
# and complete the update method.
#
# Note that the size of the occupancy grid can be changed (see below)
# as well as the update frequency of the map, and whether or not a
# map is generated. Changing these values may be useful during the
# debugging phase, but ensure that the solution you submit generates
# an occupancy grid map of size 100x100 cells.
#
# Note that this class makes the following assumptions:
#
#	PioneerCLNav
#	============
#	You have a navigator class called PioneerCLNav that implements
#	the following methods (based on Lab Tutorial 6):
#	  - a constructor that takes two arguments, an instance of a Supervisor
#	    robot object and an instance of a PioneerSimpleProxSensors
#	  - set_goal() which defines a destination pose
#	  - update() that makes any changes necessary as part of navigation
#	You can replace these with other calls if you want to use a different
#	class or means of navigation.  Note this is NOT included.
#	Note - if you use a different class you must implement a method called
#	get_real_pose() that returns an object of type Pose representing the true
#	location of the robot.  Examples of this class are used in Lab Tutorials 3 and 6.
#
#	PioneerSimpleProxSensors
#	========================
#	You have a sensor class based on the work in Lab 5.  This is used by
#	navigator class, but could also be used by a navigator class.  Code
#	for the version used in the tutorial is included with the assignment.
#
#	Pose
#	====
#	This is the latest version of the Pose class (it includes some additional
#	methods used in Lab Tutorial 6), and is used throughout the COMP329
#	code base.  A version is included with the assignment.
#
#	OccupancyGrid
#	=============
#	You have an occupancy grid class.  The constructor takes the following
#	arguments:
#	  - an instance of a Supervisor robot object
#	  - the number of cells per meter.  The higher the number, the higher
#	    the resolution of the map.  I recommend between 5-20.
#	  - the name of the display object on the robot where the map appears
#	  - the initial pose of the robot
#	  - an instance of the PioneerSimpleProxSensors object
#
#	To update the occupancy grid, call the map() method with the current Pose
#	To draw the occupancy grid, call the paint() method
#
#
# ==============================================================

from controller import Supervisor,TouchSensor
import pioneer_clnav as pn
import pioneer_simpleproxsensors as psps
import occupancy_grid as ogrid
import math
import pose

## Install these libararies 
from sklearn.cluster import DBSCAN
import numpy as np

# ==================================================================================
# Main Methods 
# ==================================================================================  


def run_robot(robot):
    """
    Main function to control the robot. It initializes components, 
    manages navigation, and updates the occupancy grid.
    """
    # Get the time step for the simulation
    timestep = int(robot.getBasicTimeStep())

    # Initialize proximity sensors and navigation classes
    pps = psps.PioneerSimpleProxSensors(robot)
    nav = pn.PioneerCLNav(robot, pps)

    # Initialize the occupancy grid with a scale of 10 cells per meter
    occupancy_grid = ogrid.OccupancyGrid(robot, 10, "display", nav.get_real_pose(), pps)

    # Exploration variables
    unexplored_threshold = 0.5  # Threshold for identifying unexplored cells
    visited_goals = set()  # Tracks visited goals to avoid revisiting
    current_goal = None  # Stores the robot's current target goal


    def is_reachable(goal_pose):
        """
        Determines if the goal cell and its immediate neighbors are free.

        Args:
            goal_pose: The pose of the goal to check.

        Returns:
            True if the goal is reachable, False otherwise.
        """
        if goal_pose is None:
            return True

        # Compute cell size in real-world units
        x_inc = occupancy_grid.arena_width / occupancy_grid.num_row_cells
        y_inc = occupancy_grid.arena_height / occupancy_grid.num_col_cells

        # Convert goal_pose to grid indices
        col_goal = int((goal_pose.x + occupancy_grid.arena_width / 2) / x_inc)
        row_goal = int((-goal_pose.y + occupancy_grid.arena_height / 2) / y_inc)

        # Check the target cell and its immediate neighbors
        neighbors = [
            (row_goal, col_goal),  # Target cell
            (row_goal - 1, col_goal),  # Up
            (row_goal + 1, col_goal),  # Down
            (row_goal, col_goal - 1),  # Left
            (row_goal, col_goal + 1),  # Right
            (row_goal - 1, col_goal - 1),  # Top-left
            (row_goal - 1, col_goal + 1),  # Top-right
            (row_goal + 1, col_goal - 1),  # Bottom-left
            (row_goal + 1, col_goal + 1)   # Bottom-right
        ]

        # Check if any of the cells are occupied
        for row, col in neighbors:
            if 0 <= row < occupancy_grid.num_col_cells and 0 <= col < occupancy_grid.num_row_cells:
                grid_index = row * occupancy_grid.num_row_cells + col
                if occupancy_grid.grid[grid_index] >= occupancy_grid.locc:
                    return False  # Occupied, not reachable

        return True  # All cells free, reachable
        
    def find_next_goal():
        """
        Find the next goal using clustering. If no valid clusters are found,
        fallback to a nearby unexplored cell.

        Returns:
            The coordinates of the next goal.
        """
        centroid = cluster_unexplored()

        if centroid:
            print(f"Cluster found. Centroid at x={centroid[0]:.2f}, y={centroid[1]:.2f}")
            return centroid
        else:
            # Fallback to finding the closest unexplored cell
            unexplored_points = []
            x_inc = occupancy_grid.arena_width / occupancy_grid.num_row_cells
            y_inc = occupancy_grid.arena_height / occupancy_grid.num_col_cells

            for i in range(occupancy_grid.get_grid_size()):
                if abs(occupancy_grid.grid[i] - occupancy_grid.lprior) < unexplored_threshold:
                    col = i % occupancy_grid.num_row_cells
                    row = i // occupancy_grid.num_row_cells
                    x = x_inc * col - (occupancy_grid.arena_width / 2) + x_inc / 2
                    y = -(y_inc * row - (occupancy_grid.arena_height / 2)) - y_inc / 2
                    unexplored_points.append((x, y))

            if unexplored_points:
                # Select a random unexplored point as fallback
                random_point = unexplored_points[0]  # For simplicity, pick the first one or use random.choice
                print(f"Fallback goal selected at x={random_point[0]:.2f}, y={random_point[1]:.2f}")
                return random_point
            else:
                # No unexplored cells remain
                print("No unexplored cells remain.")
                return None
            
    def cluster_unexplored():
        """
        Cluster unexplored cells using DBSCAN and return the centroid 
        of the largest cluster.

        Returns:
            The coordinates of the centroid of the largest cluster.
        """
        unexplored_points = []
        x_inc = occupancy_grid.arena_width / occupancy_grid.num_row_cells
        y_inc = occupancy_grid.arena_height / occupancy_grid.num_col_cells

        # Collect unexplored cells
        for i in range(occupancy_grid.get_grid_size()):
            if abs(occupancy_grid.grid[i] - occupancy_grid.lprior) < unexplored_threshold:
                col = i % occupancy_grid.num_row_cells
                row = i // occupancy_grid.num_row_cells
                x = x_inc * col - (occupancy_grid.arena_width / 2) + x_inc / 2
                y = -(y_inc * row - (occupancy_grid.arena_height / 2)) - y_inc / 2
                unexplored_points.append([x, y])

        if not unexplored_points:
            return None

        # Perform clustering
        clustering = DBSCAN(eps=0.5, min_samples=5).fit(unexplored_points)
        labels = clustering.labels_
        largest_cluster = None
        max_cluster_size = 0

        # Identify the largest cluster
        for cluster_label in set(labels):
            if cluster_label == -1:  # Ignore noise
                continue
            cluster_points = [unexplored_points[i] for i in range(len(labels)) if labels[i] == cluster_label]
            if len(cluster_points) > max_cluster_size:
                largest_cluster = cluster_points
                max_cluster_size = len(cluster_points)

        if largest_cluster:
            # Compute centroid
            centroid_x = np.mean([p[0] for p in largest_cluster])
            centroid_y = np.mean([p[1] for p in largest_cluster])
            return centroid_x, centroid_y
        return None
    
    def set_goal(centroid):
        """
        Set a new goal for navigation, ensuring it is at least 20cm 
        from the current robot position.

        Args:
            centroid: Coordinates of the goal.

        Returns:
            The new goal if valid, or None otherwise.
        """
        if centroid:
            x_inc = occupancy_grid.arena_width / occupancy_grid.num_row_cells
            y_inc = occupancy_grid.arena_height / occupancy_grid.num_col_cells

            # Calculate distance to the goal
            distance_to_goal = ((nav.get_real_pose().x - centroid[0]) ** 2 +
                                (nav.get_real_pose().y - centroid[1]) ** 2) ** 0.5

            # If the new goal is too close, find an empty cell farther away
            if distance_to_goal <= 0.2:  # 20cm threshold
                print(f"Goal at x={centroid[0]:.2f}, y={centroid[1]:.2f} is too close. Searching for a new goal...")

                unexplored_points = []
                for i in range(occupancy_grid.get_grid_size()):
                    if abs(occupancy_grid.grid[i] - occupancy_grid.lprior) < unexplored_threshold:
                        col = i % occupancy_grid.num_row_cells
                        row = i // occupancy_grid.num_row_cells
                        x = x_inc * col - (occupancy_grid.arena_width / 2) + x_inc / 2
                        y = -(y_inc * row - (occupancy_grid.arena_height / 2)) - y_inc / 2

                        # Calculate distance to this unexplored point
                        distance = ((nav.get_real_pose().x - x) ** 2 + (nav.get_real_pose().y - y) ** 2) ** 0.5

                        # Add points farther than 20cm
                        if distance > 0.2:
                            unexplored_points.append((x, y))

                if unexplored_points:
                    # Select the first unexplored point that meets the criteria
                    centroid = unexplored_points[0]
                    print(f"New goal selected at x={centroid[0]:.2f}, y={centroid[1]:.2f}")

            # Set the goal
            new_goal = pose.Pose(centroid[0], centroid[1], 0)
            nav.set_goal(new_goal)
            visited_goals.add((centroid[0], centroid[1]))
            return new_goal

        return None


    ##start 
    current_goal = set_goal(cluster_unexplored())
    if not current_goal:
        print("No valid unexplored clusters found. Exploration complete!")
        return

    movement_counter = 0
    while robot.step(timestep) != -1:
        v = pps.ts.getValue()
        if v > 0:
            movement_counter = 50

        if movement_counter == 0:
            if current_goal is None or not is_reachable(current_goal):
                print("Current goal not reachable or None. Finding new goal...")
                current_goal = set_goal(find_next_goal())
                if not current_goal:
                    if occupancy_grid.get_coverage() >= 99.0:
                        print("Exploration complete! 99% or more explored.")
                        nav.set_velocity(0,0)
                        break
                    else:
                        print("No valid goal found.")
                        continue

            if current_goal and nav.update():
                print(f"Goal reached: x={current_goal.x:.2f}, y={current_goal.y:.2f}, theta={current_goal.theta:.2f}")
                current_goal = set_goal(find_next_goal())
                if not current_goal:
                    if occupancy_grid.get_coverage() >= 99.0:
                        print("Exploration complete! 99% or more explored.")
                        nav.set_velocity(0,0)
                        break
                    else:
                        print("No valid goal found.")
                        continue
        elif movement_counter >= 39: #move backward 
            nav.set_velocity(-nav.START_VEL, -nav.START_VEL)
            movement_counter -= 1
        elif movement_counter >= 19:#Turn right
            nav.set_velocity(nav.START_VEL, -nav.START_VEL / 2)
            movement_counter -= 1
        else:#move forward
            nav.set_velocity(nav.START_VEL, nav.START_VEL)
            movement_counter -= 1

        occupancy_grid.map(nav.get_real_pose())
        occupancy_grid.paint()

        explored_percentage = occupancy_grid.get_coverage()
        #print(f"Explored Percentage: {explored_percentage:.2f}%")
        if explored_percentage >= 99.0:
            print("Exploration complete! 99% or more explored.")
            nav.set_velocity(0,0)
            break

            
if __name__ == "__main__":
    # ---------------------------------------------------------------------------
    # create the Supervised Robot instance.
    # ---------------------------------------------------------------------------
    my_robot = Supervisor()
    
    run_robot(my_robot)