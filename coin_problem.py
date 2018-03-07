#!/bin/python3

def make_changes(n, coins):
    if n <= 5:
        if n == 2 or n == 3:
            print("Give out 1 cent.\n") * n
        else:
            print("Give out {} cents.".format(n))
    else:
        if coins[n] - coins[n-1] == 1:
            print("Give out 1 cent.")
            make_changes(n - 1, coins)
        elif coins[n] - coins[n-4] == 1:
            print("Give out 4 cents.")
            make_changes(n - 4, coins)
        else:
            print("Give out 5 cents.")
            make_changes(n - 5, coins)


def make_change(n, coins):
    if n <= 5:
        return coins[n]
    else:
        for i in range(6,n+1):
            coins.append(min(1 + coins[i-1], 1 + coins[i-4], 1 + coins[i-5]))

    return coins[n]

def main():
    print("Coin Problem:")

    # available coins : 1,4,5 cents
    coins = [0, 1, 2, 3, 1, 1]
    n = 17
    result = make_change(n, coins)
    print("Result: {}".format(result))
    make_changes(n,coins)


if __name__ == "__main__":
    main()