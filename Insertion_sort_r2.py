#!/bin/python3


def insertion_sort(arr,n):
    if n == 1:
        return
    else:
        insertion_sort(arr, n-1)
        key = arr[n-1]
        j = n-2
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key
        return

arr = []

if __name__ == "__main__":
    print("Insert the array:")
    n = int(input())
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input())
       arr.append(arr_t)
    insertion_sort(arr, len(arr))
    print (" ".join(map(str, arr)))

