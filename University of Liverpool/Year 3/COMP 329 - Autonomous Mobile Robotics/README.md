# Webots Exploration and Mapping Assignment

## Overview
This project focuses on developing an autonomous robot for exploration and mapping using the Webots simulation environment. It leverages various SLAM techniques, path planning algorithms, and motion control methods to generate occupancy maps.

## Features
- **Autonomous navigation** using PID controllers and odometry
- **SLAM (Simultaneous Localization and Mapping)** integration
- **Occupancy grid mapping** for environment representation
- **Path planning** with A* or RRT algorithms
- **Data logging and visualization** of sensor readings

## Installation

### Prerequisites
Ensure you have the following installed:
- Webots
- Python 3.9+
- Required Python packages:
  ```bash
  pip install pybullet numpy matplotlib opencv-python pyqt5
  ```

### Running the Simulation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Webots-Exploration-Mapping.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Webots-Exploration-Mapping
   ```
3. Launch Webots:
   ```bash
   webots worlds/your_world.wbt
   ```
4. Run the controller script:
   ```bash
   python controllers/exploration_controller.py
   ```

## Usage
- Adjust simulation parameters in `config.json`
- Modify PID control gains for tuning in `pid_controller.py`
- Visualize occupancy maps in `map_visualizer.py`

## File Structure
```
Webots-Exploration-Mapping/
│── controllers/
│   ├── exploration_controller.py  # Main robot control script
│   ├── pid_controller.py          # PID implementation for motion control
│── maps/
│   ├── occupancy_map.png          # Generated occupancy grid
│── worlds/
│   ├── your_world.wbt             # Webots simulation world
│── utils/
│   ├── map_visualizer.py          # Visualization tools
│── config.json                     # Configuration settings
│── README.md
```

## Troubleshooting
- If `ModuleNotFoundError` occurs, ensure dependencies are installed correctly.
- If Webots crashes, check system memory and Webots version.

## License
This project is licensed under the MIT License.
