# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        totalCount = 0

        def dfs(node, maxSoFar):
            nonlocal totalCount
            if not node:
                return

            print(f"Checking {node.val} with maxSoFar = {maxSoFar}")
            
            if node.val >= maxSoFar:
                totalCount += 1
                maxSoFar = node.val
            
            dfs(node.left, maxSoFar)
            dfs(node.right, maxSoFar)
        
        dfs(root, root.val)
        return totalCount