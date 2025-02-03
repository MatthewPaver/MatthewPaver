from controller import Robot, Motor
from enum import Enum
import math

class MoveState(Enum):
    FORWARD = 1
    ROTATE = 2

WHEEL_RADIUS = 0.0975 # in meters
AXEL_LENGTH = 0.31 # in meters

def forward(target_dist, linear_velocity):
    global state
    av = (linear_velocity / WHEEL_RADIUS)
    left_motor.setVelocity(av)
    right_motor.setVelocity(av)
    state = MoveState.FORWARD
    return 1000.0 * (target_dist / linear_velocity)

def rotate(rads, linear_velocity):
    global state
    circle_fraction = rads / (2.0 * math.pi)
    circumference = math.pi * AXEL_LENGTH
    target_dist = circumference * circle_fraction
    av = (linear_velocity / WHEEL_RADIUS)
    left_motor.setVelocity(av)
    right_motor.setVelocity(-av)
    state = MoveState.ROTATE
    return 1000.0 * (target_dist / linear_velocity)

def stop():
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

# ----------------------------------------

def run_Robot(robot):
    global left_motor
    global right_motor
    global state
    av = 2 * math.pi # angular velocity
    time_elapsed = 0
    linear_velocity = 0.3
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    # enable motors
    left_motor = robot.getDevice('left wheel')
    right_motor = robot.getDevice('right wheel')
    # set target positions for motors
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    # start moving forward
    target_time = forward(2.0, linear_velocity)
    # Main loop:
    while robot.step(timestep) != -1:
        if (time_elapsed > target_time):
            stop()
            time_elapsed = 0
            if (state == MoveState.FORWARD):
                target_time = rotate(math.pi / 2.0, linear_velocity)
            elif (state == MoveState.ROTATE):
                target_time = forward(2.0, linear_velocity)
        else:
            time_elapsed += timestep # Increment by the time state

# ----------------------------------------

if __name__ == "__main__":
    # create the Robot instance.
    my_robot = Robot()
    run_Robot(my_robot)