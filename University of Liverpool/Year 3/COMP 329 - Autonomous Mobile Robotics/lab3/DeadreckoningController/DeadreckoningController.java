// File: DeadreckoningController.java
// Description: Main controller for dead reckoning with a state machine.
// Author: Your Name

import com.cyberbotics.webots.controller.Supervisor;
import com.cyberbotics.webots.controller.Display;

public class DeadreckoningController {

    public static void main(String[] args) {

        Supervisor robot = new Supervisor();
        int timeStep = (int) Math.round(robot.getBasicTimeStep());

        PioneerNav1 nav = new PioneerNav1(robot);

        double time_elapsed = 0;
        double target_time = 0;
        double robot_velocity = 0.3;

        // Define schedule of actions
        PioneerNav1.MoveState[] schedule = { 
            PioneerNav1.MoveState.CONFIGURE, 
            PioneerNav1.MoveState.FORWARD, 
            PioneerNav1.MoveState.ARC, 
            PioneerNav1.MoveState.STOP 
        };
        int schedule_index = 0; // Start with the first action in the schedule

        String display_action = "";

        // Initialize the first action if it's CONFIGURE
        if (schedule[0] == PioneerNav1.MoveState.CONFIGURE) {
            nav.configure_initialise_parameters(2 * Math.PI);
            display_action = "Configuring...";
        }

        while (robot.step(timeStep) != -1) {
            PioneerNav1.MoveState state = nav.getState();

            // Handle different robot states
            if (state == PioneerNav1.MoveState.CONFIGURE) {
                display_action = nav.configure_check_parameters(timeStep);

                // If configuration is complete, move to next action in the schedule
                if (nav.getState() == PioneerNav1.MoveState.STOP) {
                    schedule_index = (schedule_index + 1) % schedule.length;
                    state = schedule[schedule_index];
                    nav.setState(state); // Manually set the state for the next action
                }

            } else if (state == PioneerNav1.MoveState.FORWARD) {
                target_time = nav.forward(0.5, robot_velocity); // Move forward 0.5 meters
                display_action = "Moving Forward 0.5m";

                // Check if the forward action duration has passed
                if (time_elapsed >= target_time) {
                    nav.stop();
                    time_elapsed = 0;
                    schedule_index = (schedule_index + 1) % schedule.length;
                    state = schedule[schedule_index];
                    nav.setState(state);
                }

            } else if (state == PioneerNav1.MoveState.ARC) {
                target_time = nav.arc(Math.PI / 2, 0.7, robot_velocity); // Arc around ICR 0.7m away
                display_action = "Arcing around ICR";

                // Check if the arc action duration has passed
                if (time_elapsed >= target_time) {
                    nav.stop();
                    time_elapsed = 0;
                    schedule_index = (schedule_index + 1) % schedule.length;
                    state = schedule[schedule_index];
                    nav.setState(state);
                }

            } else if (state == PioneerNav1.MoveState.STOP) {
                nav.stop();
                display_action = "Stopped";

                // After stopping, cycle back to the first action or end the program
                schedule_index = 0;
                nav.setState(schedule[schedule_index]);
            }

            // Increment elapsed time only if not in CONFIGURE state
            if (state != PioneerNav1.MoveState.CONFIGURE) {
                time_elapsed += timeStep;
            }

            // Output current action and true pose
            Pose true_pose = nav.get_real_pose();
            System.out.println("Action: " + display_action + " \t" + "True Pose: " + true_pose);
        }
    }
}
