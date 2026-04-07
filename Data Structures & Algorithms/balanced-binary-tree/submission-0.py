# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        flgBalanced = True

        def getHeight(node: Optional[TreeNode]) -> int:
            nonlocal flgBalanced
            if not node:
                return 0
            
            left, right = getHeight(node.left), getHeight(node.right)
            if abs(left - right) > 1:
                flgBalanced = False
            
            return max(left, right) + 1
        
        getHeight(root)
        return flgBalanced