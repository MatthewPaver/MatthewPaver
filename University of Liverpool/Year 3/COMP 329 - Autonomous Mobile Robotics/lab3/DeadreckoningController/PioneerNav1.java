// PioneerNav1.java

import com.cyberbotics.webots.controller.Motor;
import com.cyberbotics.webots.controller.Supervisor;
import com.cyberbotics.webots.controller.Node;

public class PioneerNav1 {

  public static enum MoveState {
    STOP,
    FORWARD,
    ARC,
    CONFIGURE
  };

  private Supervisor robot;
  private Node robot_node;
  private Pose robot_pose;
  private Motor left_motor;
  private Motor right_motor;
  private String configure_str; 
  private MoveState state;

  private double velocity;
  private double config_max_x;
  private double config_min_x;
  private double config_timer;
  private double config_prev_theta;

  private final double WHEEL_RADIUS = 0.0975;
  private final double AXEL_LENGTH = 0.31;

  // Constructor
  public PioneerNav1(Supervisor robot) {
    this.robot = robot;
    this.robot_node = this.robot.getSelf();
    this.robot_pose = this.get_real_pose();
    this.state = MoveState.CONFIGURE;
    this.configure_str = "Configuring...";

    this.left_motor = robot.getMotor("left wheel");
    this.right_motor = robot.getMotor("right wheel");
    this.left_motor.setPosition(Double.POSITIVE_INFINITY);
    this.right_motor.setPosition(Double.POSITIVE_INFINITY);

    this.left_motor.setVelocity(0.0);
    this.right_motor.setVelocity(0.0);
  }

  public Pose get_real_pose() {
    if (this.robot_node == null) return new Pose(0, 0, 0);

    double[] realPos = robot_node.getPosition();
    double[] rot = this.robot_node.getOrientation();
    double theta1 = Math.atan2(-rot[0], rot[3]);
    double halfPi = Math.PI / 2;
    double theta2 = theta1 + halfPi;
    if (theta1 > halfPi) theta2 = -(3 * halfPi) + theta1;

    return new Pose(realPos[0], realPos[1], theta2);
  }

  public void configure_initialise_parameters(double icr_omega) {
    // This rotates the robot about one wheel, and monitors time and distance
    this.velocity = icr_omega;
    this.config_max_x = robot_pose.getX();
    this.config_min_x = robot_pose.getX();
    this.config_timer = 0;
    this.config_prev_theta = robot_pose.getTheta();

    // Set motor velocities to initiate configuration
    this.left_motor.setVelocity(0);
    this.right_motor.setVelocity(this.velocity);
    this.state = MoveState.CONFIGURE;
  }

  public String configure_check_parameters(double timestep) {
    Pose pose = this.get_real_pose();
    this.config_timer += timestep;

    double axel_length = this.config_max_x - this.config_min_x;

    // Check if a full rotation is completed
    if ((this.config_prev_theta < 0) && (pose.getTheta() >= 0.0)) {
      // Calculate the wheel radius
      double distance = axel_length * 2 * Math.PI;
      double wheel_radius = distance / (this.velocity * (this.config_timer / 1000));
      this.configure_str = String.format("Configuration Complete - Axel Length: %.3f, Wheel Radius: %.3f", axel_length, wheel_radius);

      // Set to next state, e.g., STOP or another scheduled state
      this.state = MoveState.STOP;
    } else {
      // Update max/min x for determining circle diameter
      this.config_max_x = Math.max(this.config_max_x, pose.getX());
      this.config_min_x = Math.min(this.config_min_x, pose.getX());
      this.config_prev_theta = pose.getTheta();
    }

    return this.configure_str;
  }

  public void stop() {
    this.left_motor.setVelocity(0.0);
    this.right_motor.setVelocity(0.0);
    this.state = MoveState.STOP;
  }

  public MoveState getState() {
    return this.state;
  }
}
