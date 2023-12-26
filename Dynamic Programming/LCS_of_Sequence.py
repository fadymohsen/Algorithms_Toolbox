def lcs3(first_sequence, second_sequence, third_sequence):
    m, n, o = len(first_sequence), len(second_sequence), len(third_sequence)

    # Creating a 3D array to store the lengths of LCS solutions of subproblems
    L = [[[0 for _ in range(o+1)] for _ in range(n+1)] for _ in range(m+1)]

    # Building the 3D array from the bottom up
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if i == 0 or j == 0 or k == 0:
                    L[i][j][k] = 0
                elif (first_sequence[i-1] == second_sequence[j-1] and
                      first_sequence[i-1] == third_sequence[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(max(L[i-1][j][k], L[i][j-1][k]), L[i][j][k-1])

    # Length of the longest common subsequence is found at L[m][n][o]
    return L[m][n][o]

















if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
