#!/bin/python3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def displayTreeFileStructure(self, root, level):

        if root == None:
            return []

        space = ""
        for i in range(level):
            if i%level == 0 or i%level == (level-1):
                space += "\t|"
            else:
                space += "\t"

        space += "---"+str(root.val)
        print(space)
        level += 1
        self.displayTreeFileStructure(root.left, level)
        self.displayTreeFileStructure(root.right, level)

    def displayTreeBranch(self, root, level, child):

        if root == None:
            return []

        self.displayTreeBranch(root.left, level + 1, 0)
        sstr = ""

        if child == 1:
            sstr += "|\t" * (level-1) + "|"

        if level != 1:
            sstr += "\t" * level + "|=>"
        else:
            sstr += "\t|=>"

        sstr += str(root.val)

        if root.left != None or root.right != None:
            sstr += "|"

        print(sstr)
        self.displayTreeBranch(root.right, level + 1, 1)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        pList = []

        pList.append(root.val)
        pList += self.preorderTraversal(root.left)
        pList += self.preorderTraversal(root.right)

        return pList

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        pList = []

        pList += self.inorderTraversal(root.left)
        pList.append(root.val)
        pList += self.inorderTraversal(root.right)

        return pList

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        pList = []

        pList += self.postorderTraversal(root.left)
        pList += self.postorderTraversal(root.right)
        pList.append(root.val)

        return pList


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
    print("Tree in File structure display:")
    sol.displayTreeFileStructure(root, 0)

    print("Tree in branch structure display:")
    #sol.displayTreeBranch(root, 0, 0)

    pre_order = sol.preorderTraversal(root)
    print ("Pre Order traversal:")
    print(pre_order)

    pre_order = sol.inorderTraversal(root)
    print ("In Order traversal:")
    print(pre_order)

    pre_order = sol.postorderTraversal(root)
    print ("Post Order traversal:")
    print(pre_order)


if __name__ == "__main__":
    main()
