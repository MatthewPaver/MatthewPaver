def min_value_grouping():
    
    """
    This function computes the minimum value of the objective function
    for grouping an array into k groups, along with the cutting positions.

    The dynamic programming approach is used where dp[i][j] represents
    the minimum value for the first i numbers grouped into j groups.
    A cumulative sum array is used for efficient calculation of group sums.

    Time Complexity: O(kn^2), due to three nested loops iterating up to k, n, and n.
    Space Complexity: O(nk), for the dynamic programming table and cumulative sum array.

    :param n: Total number of elements in the array.
    :param k: Number of groups to divide the array into.
    :param arr: List of positive integers representing the array.
    :return: Tuple of the minimum objective value and list of cutting positions.
    """
       
    # Read the number of elements (n), the number of groups (k), and the sequence of numbers (arr)
    # from standard input. Expecting three lines of input.
    n = int(input().strip())
    k = int(input().strip())
    arr = list(map(int, input().strip().split()))

    # Calculate the cumulative sum of the sequence to facilitate easy range sum calculations later.
    sum_cubes = [0] * (n + 1)  # sum_cubes[i] will store the sum of arr[0] to arr[i-1].
    for i in range(1, n + 1):
        sum_cubes[i] = sum_cubes[i - 1] + arr[i - 1]

    # Initialize the dynamic programming table 'dp'.
    # dp[i][j] will hold the minimum objective value for partitioning the first 'i' numbers into 'j' groups.
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: No groups means zero value.

    # Populate the DP table using the bottom-up approach.
    # For each number of groups 'j' and for each 'i' numbers, find the minimum value.
    for j in range(1, k + 1):
        for i in range(j, n + 1):
            # Explore all possible previous group end positions 'x' for the current group start.
            for x in range(j - 1, i):
                # Calculate the value of the current group and update the DP table if it's a new minimum.
                group_sum = sum_cubes[i] - sum_cubes[x]
                dp[i][j] = min(dp[i][j], dp[x][j - 1] + group_sum ** 3)

    # Backtracking to find the cutting points starting from the last element and the last group.
    cuts = []  # This list will store the indices where the cuts will be made.
    temp = dp[n][k]  # Start with the minimum value of the last group.
    j = k  # Start backtracking from the last group.
    for i in range(n, 0, -1):
        if dp[i][j] == temp:  # Check if this position is part of the solution.
            # Look for the position 'x' where the cut can be made.
            for x in range(i, 0, -1):
                if dp[x][j - 1] + (sum_cubes[i] - sum_cubes[x]) ** 3 == temp:
                    cuts.append(x)  # Found a cut point, add to the cuts list.
                    temp = dp[x][j - 1]  # Update the remaining value to find the next cut point.
                    j -= 1  # Move to the previous group.
                    break  # We've found the cut for this group, move to the previous one.

    # Output the result.
    # First, print the minimum value of the objective function.
    print(dp[n][k])
    # Then, print the list of cutting points, which are indices that separate the numbers into groups.
    # Include 0 (start of the array) and 'n' (end of the array) as specified in the problem statement.
    print([0] + cuts[::-1] + [n])

# Call the min_value_grouping function to execute the grouping algorithm.
min_value_grouping()
