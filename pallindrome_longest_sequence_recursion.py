#!/bin/python3


def long_sequence_recursion(str, i, j):
    if i == j:
        # single character
        return 1
    elif (i + 1 == j) and (str[i] == str[j]):
        # 2 same characters
        return 2
    elif str[i] == str[j]:
        # first and last characters are same
        return long_sequence_recursion(str, i + 1, j - 1) + 2
    else:
        # first and last characters are not same
        return max(long_sequence_recursion(str, i + 1, j), long_sequence_recursion(str, i, j - 1))


def main():
    print("Longest Pallindrome sequence Problem: Recursive solution")
    test_str = "character"

    result = long_sequence_recursion(test_str, 0, len(test_str) - 1)
    print("Result: {}".format(result))


if __name__ == "__main__":
    main()
