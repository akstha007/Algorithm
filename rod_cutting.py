#!/bin/python3
# Rod cutting problem: Dynamic programming
# get the maximum profit for selling particular piece of rod which can be cut
# into any no. of pieces to gain maximum profit.


def cut_rod(n):
    profit = [0] * (n+1)
    for i in range(1,n+1):
        max_profit = 0;
        for j in range(i):
            max_profit = max(max_profit, price[j] + profit[i-j-1])
        profit[i] = max_profit

    return profit[n]


length = [1,2,3,4,5,6,7,8,9,10]
price = [1,5,8,9,10,17,17,20,24,30]

if __name__ == "__main__":
    print("Manhattan Graph: Dynamic Programming")
    result = cut_rod(4)
    print("Result: {}".format(result))
