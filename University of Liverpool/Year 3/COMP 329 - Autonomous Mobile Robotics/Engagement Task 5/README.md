# Engagement Task 5 - Grid Localisation

## Objective
The objective of this task is to simulate a scenario where a robot is navigating in a 20-cell space, starting from a known position and adjusting its belief about its location through movements forward and backward.

## Implementation
The implementation involves:
1. Initializing the belief distribution with full confidence at the starting position.
2. Applying movement probabilities to update the belief distribution.
3. Normalizing the belief distribution after each update.
4. Handling boundary conditions to ensure probabilities do not leak beyond the range of cells.

## Usage
To run the simulation, execute the provided Python script `Engagement Task 5.py`. The script will print the belief distribution after each move, showing the most likely position and the true position.

## Files
- `Engagement Task 5.py`: The main script that performs the grid localization task.
- `Engagement Task 5 Summary.txt`: A summary of the task, including observations and methodology.

## Example Output
The script will output the belief distribution in the following format:
```
Move 1: |0.000|0.000|0.000|0.000|0.000|0.000|0.000|0.000|0.000|0.000|1.000|0.000|0.000|0.000|0.000|0.000|0.000|0.000|0.000|0.000| pTotal = 1.000 likelyPos = 10 truePos = 10
Move 2: |0.000|0.000|0.000|0.000|0.000|0.000|0.000|0.000|0.000|0.250|0.500|0.250|0.000|0.000|0.000|0.000|0.000|0.000|0.000|0.000| pTotal = 1.000 likelyPos = 10 truePos = 11
...
```

## License
This project is licensed under the MIT License.
