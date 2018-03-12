#!/bin/python3

def get_substring(L, i, j):
    if L[i][j] > 0:
        if L[i][j] == L[i + 1][j]:
            get_substring(L, i + 1, j)
        elif L[i][j] == L[i][j-1]:
            get_substring(L, i, j-1)
        else:
            result_substring[i] = test_str[i]
            result_substring[j] = test_str[j]
            get_substring(L, i + 1, j - 1)


def long_sequence_dynamic(str):

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

    for row in L:
        print(row)

    return L[0][n - 1]


test_str = "characters"
n = len(test_str)
L = [[0 for _ in range(n)] for _ in range(n)]

result_substring = ["" for _ in range(n)]


def main():
    print("Longest Pallindrome sequence Problem: Dynamic solution")
    print(list(test_str))
    result = long_sequence_dynamic(test_str)
    print("Result: {}".format(result))

    get_substring(L, 0, n - 1)
    print("".join(result_substring))


if __name__ == "__main__":
    main()
