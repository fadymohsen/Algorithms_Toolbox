from sys import stdin

def partition3(values):
    total_value = sum(values)
    n = len(values)

    # If total value is not divisible by 3, it's impossible to partition
    if total_value % 3 != 0:
        return 0

    third_value = total_value // 3

    # Create a 3D dynamic programming table
    dp = [[[0 for _ in range(third_value + 1)] for _ in range(third_value + 1)] for _ in range(n + 1)]

    # Initialize the dp table for the base case
    dp[0][0][0] = 1

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(third_value + 1):
            for k in range(third_value + 1):
                # If the i-th souvenir is not included in any subset
                dp[i][j][k] = dp[i-1][j][k]

                # If the i-th souvenir is included in the first subset
                if j >= values[i-1]:
                    dp[i][j][k] |= dp[i-1][j - values[i-1]][k]

                # If the i-th souvenir is included in the second subset
                if k >= values[i-1]:
                    dp[i][j][k] |= dp[i-1][j][k - values[i-1]]

    # Check if partitioning into 3 subsets with equal sum is possible
    return 1 if dp[n][third_value][third_value] else 0





if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)

    print(partition3(input_values))
