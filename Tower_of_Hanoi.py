#!/bin/python3


def tower_of_hanoi(n, source, dest, aux):
    if n==1:
        print("Move plate {} from {} to {}".format(n,source,dest))
        return 1
    else:
        steps = 0
        steps += tower_of_hanoi(n-1,source,aux,dest)
        print("Move plate {} from {} to {}".format(n, source, dest))
        steps += 1
        steps += tower_of_hanoi(n-1,aux,dest,source)
    return steps


if __name__ == "__main__":
    print("Insert the no. of plates in Tower of Hanoi:")
    n = int(input())
    steps = tower_of_hanoi(n,"Tower 1", "Tower 2", "Tower 3")
    print("No. of steps: {}".format(steps))


