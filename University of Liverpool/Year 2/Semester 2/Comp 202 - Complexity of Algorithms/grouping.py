def min_value_grouping():
    """
    This function computes the minimum value of the objective function
    for grouping an array into k groups, along with the cutting positions.

    The dynamic programming approach is used where dp[i][j] represents
    the minimum value for the first i numbers grouped into j groups.
    A cumulative sum array is used for efficient calculation of group sums.

    Time Complexity: O(kn^2), due to three nested loops iterating up to k, n, and n.
    Space Complexity: O(nk), for the dynamic programming table and cumulative sum array.

    :return: Tuple of the minimum objective value and list of cutting positions.
    """
    # Read the number of elements and groups from input
    n = int(input())
    k = int(input())
    # Read the sequence of numbers from input
    arr = [int(i) for i in input().split()]

    # Initialise the cumulative sum array
    sum_cubes = [0] * (n + 1)
    # Calculate the cumulative sum
    for i in range(1, n + 1):
        sum_cubes[i] = sum_cubes[i - 1] + arr[i - 1]

    # Initialise the dynamic programming table with infinity
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    # The minimum value for 0 numbers grouped into 0 groups is 0
    dp[0][0] = 0

    # Populate the dynamic programming table
    for j in range(1, k + 1):
        for i in range(j, n + 1):
            for x in range(j - 1, i):
                # Calculate the sum of the group
                group_sum = sum_cubes[i] - sum_cubes[x]
                # Update the minimum value for the first i numbers grouped into j groups
                dp[i][j] = min(dp[i][j], dp[x][j - 1] + group_sum ** 3)

    # Initialise the list of cutting positions
    cuts = []
    # Start from the minimum value for the whole sequence grouped into k groups
    temp = dp[n][k]
    j = k
    # Backtrack to find the cutting positions
    for i in range(n, 0, -1):
        if dp[i][j] == temp:
            for x in range(i, 0, -1):
                if dp[x][j - 1] + (sum_cubes[i] - sum_cubes[x]) ** 3 == temp:
                    # Add the cutting position to the list
                    cuts.append(x)
                    # Move to the previous group
                    temp = dp[x][j - 1]
                    j -= 1
                    break

    # Print the minimum value of the objective function
    print(dp[n][k])
    # Print the list of cutting positions
    print([0] + cuts[::-1] + [n])

# Call the function
min_value_grouping()
