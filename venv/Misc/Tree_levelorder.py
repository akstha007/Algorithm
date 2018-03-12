#!/bin/python3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def treeHeight(self, root):
        if root == None:
            return 1
        left_height = self.treeHeight(root.left)
        right_height = self.treeHeight(root.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def printLevelOrder(self, root, level, node_list):
        if root == None:
            return
        if level == 1:
            print(root.val)
            node_list.append(root.val)
        else:
            self.printLevelOrder(root.left, level - 1, node_list)
            self.printLevelOrder(root.right, level - 1, node_list)

    def levelOrder(self, root, height):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return[]

        bfs = []

        for i in range(1, height):
            node_list = []
            self.printLevelOrder(root, i, node_list)
            bfs.append(node_list)

        return bfs


def main():
    print("Tree:")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right.right = TreeNode(7)

    sol = Solution()
    print("Height of tree:")
    height = sol.treeHeight(root)
    print(height)

    level_order = sol.levelOrder(root, height)
    print ("Level Order traversal / Breadth first Search:")
    print(level_order)


if __name__ == "__main__":
    main()
