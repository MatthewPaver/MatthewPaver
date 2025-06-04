import os
import sys

# Add path to occupancy_grid module
MODULE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "University of Liverpool",
    "Year 3",
    "COMP 329 - Autonomous Mobile Robotics",
    "Assignment 1",
    "occupancy_map",
    "controllers",
    "my_assignment_controller",
)
sys.path.append(os.path.abspath(MODULE_PATH))

import occupancy_grid
import pose


class DummyField:
    def __init__(self, value):
        self._value = value

    def getSFVec2f(self):
        return self._value


class DummyArena:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getField(self, name):
        if name == "floorSize":
            return DummyField([self.width, self.height])
        raise AttributeError(name)


class DummyDisplay:
    def getWidth(self):
        return 10

    def getHeight(self):
        return 10


class Robot:
    def __init__(self, width=1.0, height=1.0):
        self._arena = DummyArena(width, height)
        self._display = DummyDisplay()

    def getFromDef(self, name):
        if name == "ARENA":
            return self._arena
        return None

    def getDevice(self, name):
        return self._display


class ProxSensor:
    def get_radius(self):
        return 0.1


def test_get_cell_probability_at_pose():
    robot = Robot()
    prox = ProxSensor()
    grid = occupancy_grid.OccupancyGrid(robot, 1, "display", pose.Pose(), prox)

    grid.grid[0] = 1.23  # non-default log-odds value
    expected = grid.cell_probability(grid.grid[0])

    prob = grid.get_cell_probability_at_pose(pose.Pose(0, 0, 0))

    assert prob == expected
