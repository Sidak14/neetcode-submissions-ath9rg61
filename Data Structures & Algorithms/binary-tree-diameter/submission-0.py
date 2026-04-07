# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root: Optional[TreeNode], maxDiameter: List[int]) -> int:
        if not root:
            return 0

        leftHeight, rightHeight = self.getHeight(root.left, maxDiameter), self.getHeight(root.right, maxDiameter)
        d = leftHeight + rightHeight
        if d > maxDiameter[0]:
            maxDiameter[0] = d
        return max(leftHeight, rightHeight) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDiameter = [0]
        leftHeight, rightHeight = self.getHeight(root.left, maxDiameter), self.getHeight(root.right, maxDiameter)
        d = leftHeight + rightHeight
        if d > maxDiameter[0]:
            maxDiameter[0] = d
        
        return maxDiameter[0]