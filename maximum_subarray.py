#!/bin/python3

def max_subarray_lin3(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            for k in range(i, j):
                sum += arr[k]
                result = max(result, sum)

    return result


def max_subarray_lin2(arr):
    result = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            result = max(result, sum)

    return result


def max_subarray_recursive(arr, n):
    if n == 0:
        return arr[n]
    else:
        result = max_subarray_recursive(arr, n - 1)
        sum = 0
        for i in range(n - 1, -1, -1):
            sum += arr[i]
            result = max(result, sum)
        return result


def max_subarray_dynamic(arr):
    result = 0
    ms = [0 for _ in range(len(arr) + 1)]
    for i in range(1, len(arr)):
        ms[i] = max(arr[i - 1], arr[i - 1] + ms[i - 1])
        result = max(result, ms[i])

    return result


def main():
    print("Maximum Subarray Problem:")

    # available coins : 1,4,5 cents
    arr = [0, 1, 2, 3, 1, 1, -1, -10, 9, 10, 9, -6]

    result = max_subarray_lin3(arr)
    print("Result Brute Force O(n^3): {}".format(result))

    result = max_subarray_lin2(arr)
    print("Result Brute Force O(n^2): {}".format(result))

    result = max_subarray_recursive(arr, len(arr))
    print("Result Recursion O(n lg n): {}".format(result))

    result = max_subarray_dynamic(arr)
    print("Result Dynamic O(n): {}".format(result))


if __name__ == "__main__":
    main()
