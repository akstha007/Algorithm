#!/bin/python3


def partition(arr, low, high):
    pivot = arr[high-1]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]

    arr[i+1], arr[high-1] = arr[high-1], arr[i+1]

    return i+1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)


arr = []


if __name__ == "__main__":
    print("Insert the array:")
    n = int(input())
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input())
       arr.append(arr_t)
    quick_sort(arr, 0, len(arr))
    print (" ".join(map(str, arr)))

