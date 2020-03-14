# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """ This is a classical problem that I've seen many times before.
            Solution 1: Simple recursion, check entire BST
        """
        # if root is None: return 0
        # return (root.val if L <= root.val <= R else 0) + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        """ Optimized solution 1: In-order tree traversal; only evaluate nodes that can be in range [L, R]
        """
        sumSoFar = 0
        if root.val > L and root.left:
            sumSoFar += self.rangeSumBST(root.left, L, R)
        if root.val >= L and root.val <= R:
            sumSoFar += root.val
        if root.val < R and root.right:
            sumSoFar += self.rangeSumBST(root.right, L, R)
        return sumSoFar