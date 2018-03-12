#!/bin/python3


def long_sequence_dynamic(str):
    n = len(str)
    L = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        L[i][i] = 1

    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            if i + 1 == j and str[i] == str[j]:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i + 1][j], L[i][j - 1])

    return L[0][n-1]


def main():
    print("Longest Pallindrome sequence Problem: Dynamic solution")
    test_str = "character"

    result = long_sequence_dynamic(test_str)
    print("Result: {}".format(result))


if __name__ == "__main__":
    main()
