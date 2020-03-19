# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def getGrandchildren(self, gp):
    #     if gp is None: return []
    #     gc = []
    #     if gp.left is not None:
    #         gc.extend([gp.left.left, gp.left.right])
    #     if gp.right is not None:
    #         gc.extend([gp.right.left, gp.right.right])
    #     gc = filter((lambda x: x is not None), gc)
    #     return list(map((lambda x: x.val), gc))

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """ Test cases:
            I: root = [2,null,null]
            O: 0

            I: root = [2,4,6,null,null,null,null]
            O: 0

            I: root = [2,1,3,1,7,9,11]
            O: 4
        """
        """ Optimized solution 1:
            - Pre-order DFS using python stacks for flair
            Time complexity: O(n)
            Runtime: 92ms
        """
        if not root: return 0  # empty tree

        # initialization:
        summation = 0

        # root node, -1 for init, -1 for init
        dfs_stack = [(root, -1, -1)]

        # pre-order DFS traveral
        while dfs_stack:
            node, parent, grandparent = dfs_stack.pop()
            if grandparent & 1 == 0: summation += node.val
            if node.right: dfs_stack.append((node.right, node.val, parent))
            if node.left: dfs_stack.append((node.left, node.val, parent))

        return summation

        """ Initial solution:
            - One solution would be to work from the top-down, seeing whether or not the node is even and adding the grandchildrens' sums to our accumulated result (if the node is a grandparent)
            - Define helper function to return list of grandchildren vals
            Time complexity: O(n) with lots of operations
            Runtime: 132ms
        """
#         if root is None: return 0
#         return self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right) + (sum(self.getGrandchildren(root)) if root.val % 2 == 0 else 0)


