# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.vals = collections.defaultdict(int)

    def sum_bst(root):
        if not root:
            return 0

        return root.val + sum_bst(root.left) + sum_bst(root.right)

    def sum_larger_vals_inc(root):
        if not root.right:
            return root.val
        elif root.right.val in self.vals
            return self.vals[root.right.val] + root.val

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """ Initial solution:
            - Post order tree traversal with memoization (keep track of mapping of node: new_val so that parents of nodes can simply add themselves to their right-child's value, greatly decreasing work)
            - Define helper function to calculate new values

        """
        if not root.right:
            self.vals[root.val] = root.val
            return root

        self.vals[root.right.val] = root.right.val +

