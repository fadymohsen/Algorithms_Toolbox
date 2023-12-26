def edit_distance(first_string, second_string):
    len_s = len(first_string) + 1
    len_t = len(second_string) + 1

    # Create a distance matrix and write in initial values.
    d = [[x] + [0] * (len_t - 1) for x in range(len_s)]
    d[0] = [x for x in range(len_t)]

    for i in range(1, len_s):
        for j in range(1, len_t):

            # Levenshtein distance calculation.
            if first_string[i - 1] == second_string[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1

    # The last element of the matrix is edit distance metric.
    return d[-1][-1]








if __name__ == "__main__":
    print(edit_distance(input(), input()))
