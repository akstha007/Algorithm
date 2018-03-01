#!/bin/python3
# Manhattan graph to find no. ways to reach from (0,0) to (m,n) in 2D graph

def manhattan_graph(m, n):
    ans = [[0] * (n+1)] * (m+1)

    # this steps can be eliminated with ans initialized with value 1
    for i in range(m+1):
        ans[i][0] = 1

    for j in range(n+1):
        ans[0][j] = 1
    # end of initialization part

    for i in range(1, m+1):
        for j in range(1, n+1):
            ans[i][j] = ans[i-1][j] + ans[i][j-1]

    return ans[m][n]


if __name__ == "__main__":
    print("Manhattan Graph")
    result = manhattan_graph(4,5)
    print("Result: {}".format(result))
