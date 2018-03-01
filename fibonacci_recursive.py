#!/bin/python3


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print("Fibonacci series using Recursive Algorithm")
    result = fib(100)
    print("Result: {}".format(result))
