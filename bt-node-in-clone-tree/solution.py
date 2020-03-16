# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """ Naive solution:
            - DFS with checking deep copy
        """
        # return self.dfs(cloned, target)
        """ Optimized solution 1:
            - Paired BFS
        """
        que = collections.deque([(original, cloned)])  # start at the root
        while que:
            nodeOrig, nodeClon = que.popleft()
            if nodeOrig is target:  # if original node is found - cloned node is our answer
                return nodeClon
            if nodeOrig.left:  que.append((nodeOrig.left, nodeClon.left))
            if nodeOrig.right: que.append((nodeOrig.right, nodeClon.right))

#     def bfs(self, tree, target):
#         if tree is None: return None
#         if tree.val == target.val:
#             if self.deepIsEqual(tree, target): return tree
#         left = self.dfs(tree.left, target)
#         if left is not None: return left
#         right = self.dfs(tree.right, target)
#         if right is not None: return right
#         return None

#     def deepIsEqual(self, n1, n2):
#         if n1 is None: return n2 is None
#         return (n1.val == n2.val) and self.deepIsEqual(n1.left, n2.left) and self.deepIsEqual(n1.right, n2.right)