#!/bin/python3


def fib(n):
    fib_list = [1] * (n+1)
    for i in range(3,n+1,1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]

    return fib_list[n]


if __name__ == "__main__":
    print("Fibonacci series using Iterative/Dynamic Algorithm")
    result = fib(100)
    print("Result: {}".format(result))
