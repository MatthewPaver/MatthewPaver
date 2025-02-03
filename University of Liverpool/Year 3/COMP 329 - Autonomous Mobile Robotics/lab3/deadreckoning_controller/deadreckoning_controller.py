# deadreckoning_controller.py

from controller import Supervisor
import pioneer_nav1 as pn
import math
from pioneer_nav1 import MoveState

def run_robot(robot):
    # Get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())

    # Initialize the PioneerNavigation class
    nav = pn.PioneerNavigation(robot)
    time_elapsed = 0
    target_time = 0
    robot_velocity = 0.3
    
    # Define schedule
    schedule = [MoveState.CONFIGURE, MoveState.FORWARD, MoveState.ARC, MoveState.STOP]
    schedule_index = 0  # Start with the first action in the schedule
    
    display_action = ""

    # Initialize the configuration if the first action is CONFIGURE
    if schedule[0] == MoveState.CONFIGURE:
        nav.configure_initialise_parameters(2 * math.pi)

    # Main control loop
    while robot.step(timestep) != -1:
        current_state = schedule[schedule_index]

        if current_state == MoveState.CONFIGURE:
            # Check configuration parameters
            display_action = nav.configure_check_parameters(timestep)
            print(f"Action: {display_action} \tTrue Pose: {nav.get_real_pose()}")
            # Once configuration is done, move to the next action
            schedule_index = (schedule_index + 1) % len(schedule)
            target_time = 0
            time_elapsed = 0

        elif current_state == MoveState.FORWARD:
            # Move the robot forward for a specified distance
            if time_elapsed == 0:
                target_time = nav.forward(0.5, robot_velocity)  # Move 0.5 meters at 0.3 m/s
                display_action = "Forward Action: Moving forward"
            time_elapsed += timestep
            print(f"Action: {display_action} \tTrue Pose: {nav.get_real_pose()}")

            # Transition to the next action after moving forward for the target time
            if time_elapsed >= target_time:
                schedule_index = (schedule_index + 1) % len(schedule)
                target_time = 0
                time_elapsed = 0

        elif current_state == MoveState.ARC:
            # Move the robot in an arc
            if time_elapsed == 0:
                target_time = nav.arc(math.pi / 2, 0.7, robot_velocity)  # Arc 90 degrees at 0.3 rad/s
                display_action = "Arc Action: Moving in an arc"
            time_elapsed += timestep
            print(f"Action: {display_action} \tTrue Pose: {nav.get_real_pose()}")

            # Transition to the next action after the arc action completes
            if time_elapsed >= target_time:
                schedule_index = (schedule_index + 1) % len(schedule)
                target_time = 0
                time_elapsed = 0

        elif current_state == MoveState.STOP:
            # Stop the robot and end the loop
            nav.stop()
            display_action = "Stop Action: Robot stopped"
            print(f"Action: {display_action} \tTrue Pose: {nav.get_real_pose()}")
            break

if __name__ == "__main__":
    # Create the Supervisor instance
    my_robot = Supervisor()
    run_robot(my_robot)
