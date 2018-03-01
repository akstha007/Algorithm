#!/bin/python3
# Rod cutting problem: Recursive solution
# get the maximum profit for selling particular piece of rod which can be cut
# into any no. of pieces to gain maximum profit.

def cut_rod(n):
    if n < 1:
        return 0
    else:
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, price[i] + cut_rod(n-i-1))

        return max_profit


length = [1,2,3,4,5,6,7,8,9,10]
price = [1,5,8,9,10,17,17,20,24,30]

if __name__ == "__main__":
    print("Manhattan Graph: Recursive Programming")
    result = cut_rod(4)
    print("Result: {}".format(result))
