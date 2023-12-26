from sys import stdin

def maximum_gold(capacity, weights):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the i-th item is not included
            dp[i][w] = dp[i-1][w]
            # If the i-th item is included (and its weight does not exceed the current capacity)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + weights[i-1])

    return dp[n][capacity]









if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
