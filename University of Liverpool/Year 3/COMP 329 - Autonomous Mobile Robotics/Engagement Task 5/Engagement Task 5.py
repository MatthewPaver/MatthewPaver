"""
Engagement Task 5 - Grid Localisation

Objective:
This task mimics a scenario where a robot is navigating in a 20 cell space, with certainty starting from position 10 and adjusting its understanding of location through movements forward and backward.

Methodology:
1)  Setting the starting belief at position 10 by initialising it as a single point mass. 
2)	Apply probabilities of [0.25, 0.5, 0.25] for moves of 0, 1, or 2 ce;;s, adjusting the belief spread without introducing randomness. 
3) 	After every update make sure that the total belief distribution adds up to 1. (Normalisation)
4) 	When dealing with boundaries make sure to consider edge cases to avoid any probabilities leaking beyond the range of cells, from 0, to 19. 


Observations:
-   The belief gradually spreads as actions are taken and the likelihood of an outcome decreases over time. Indicating a rise, in uncertainty. 
-	Near cells 18 and 19, on the edges show a focused belief distribution due to movement options available in that area; this leads to higher certainty, about the position. This shows boundary effects.
-	At Position 17; The distribution of beliefs might display unsual behavior because of the boundary effects when the robot nears the edge. 

"""


import numpy as np

# Initialize the belief distribution
belief = np.zeros(20)
belief[10] = 1.0  # Start with full confidence at position 10

# Define movement probabilities
MOVE_PROBS = [0.25, 0.5, 0.25]  # Probability to move 0, 1, or 2 cells forward

def normalize(belief):
    "Normalises the belief distribution so it sums to 1."
    total = sum(belief)
    if total > 0:
        return belief / total
    return belief

def print_belief(belief, move_count, likely_pos, true_pos):
    "Prints the belief distribution in the required format."
    formatted_belief = " | ".join(f"{p:.3f}" for p in belief)
    p_total = sum(belief)
    print(f"Move {move_count}: |{formatted_belief}| pTotal = {p_total:.3f} likelyPos = {likely_pos} truePos = {true_pos}")

def update_belief(belief, move_probs, move_direction=1):
    "Updates the belief distribution based on movement probabilities."
    new_belief = np.zeros_like(belief)
    for i in range(len(belief)):
        for j, prob in enumerate(move_probs):
            new_index = i + (j * move_direction)
            if 0 <= new_index < len(belief):
                new_belief[new_index] += belief[i] * prob
    return normalize(new_belief)

# Display initial message if required
print("Building Robot")

# Perform a series of forward moves and print the belief distribution after each move
for move_count in range(1, 10):  # Example of 9 forward moves
    belief = update_belief(belief, MOVE_PROBS, move_direction=1)
    likely_pos = np.argmax(belief)  # Get the most likely position
    true_pos = 10 + move_count      # Example true position

    # Print the formatted belief distribution
    print_belief(belief, move_count, likely_pos, true_pos)

# Perform a series of backward moves and print the belief distribution after each move
for move_count in range(1, 6):  # Example of 5 backward moves
    belief = update_belief(belief, MOVE_PROBS, move_direction=-1)
    likely_pos = np.argmax(belief)  # Get the most likely position
    true_pos = 18 - move_count      # Example true position

    # Print the formatted belief distribution
    print_belief(belief, 9 + move_count, likely_pos, true_pos)