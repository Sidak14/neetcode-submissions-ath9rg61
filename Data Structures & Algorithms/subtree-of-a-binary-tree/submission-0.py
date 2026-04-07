# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, node1, node2) -> bool:
        if not node1 and not node2:
            return True
        
        if not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False

        leftSame = self.isSameTree(node1.left, node2.left)
        if not leftSame:
            return False

        rightSame = self.isSameTree(node1.right, node2.right)
        if not rightSame:
            return False

        return True
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root:
            return False
        
        if not subRoot:
            return True
        
        if self.isSameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        if left:
            return True

        right = self.isSubtree(root.right, subRoot)
        if right:
            return True

        return False

