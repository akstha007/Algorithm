#!/bin/python3


def fib(n):
    if table[n] != -1:
        return table[n]
    else:
        if n <= 2:
            return 1
        else:
            table[n] = fib(n - 1) + fib(n - 2)
            return table[n]


num = 100

# initialize table with size num+1 with -1 value
table = [-1] * (num + 1)

if __name__ == "__main__":
    print("Fibonacci series using Recursive Table Algorithm")
    result = fib(num)
    print("Result: {}".format(result))
