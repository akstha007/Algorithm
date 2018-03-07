#!/bin/python3

def pick(n, W, v_mat):
    if v_mat[n][W] > 0:
        if v_mat[n][W] == v_mat[n - 1][W]:
            pick(n - 1, W, v_mat)
        else:
            print("Take item {}.".format(n))
            pick(n - 1, W - wt[n - 1], v_mat)


def compute_v(W, wt, val, n):
    v_mat = [[0 for x in range(W+1)] for y in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                v_mat[i][j] = 0
            elif wt[i-1] <= j:
                v_mat[i][j] = max(v_mat[i-1][j], val[i-1]+v_mat[i-1][j-wt[i-1]])
            elif wt[i-1] > j:
                v_mat[i][j] = v_mat[i-1][j]

    return v_mat


wt = [2, 1, 3, 2]
val = [12, 10, 20, 15]
n = len(val)
W = 5

def main():
    print("Knapsack Problem:")
    v_mat = compute_v(W, wt, val, n)
    print(v_mat)
    pick(n, W, v_mat)


if __name__ == "__main__":
    main()