# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        currentLevel = [root]
        output = []
        while currentLevel:
            nextLevel = []
            currentLevelVals = []
            for node in currentLevel:
                currentLevelVals.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            output.append(currentLevelVals)
            currentLevel = nextLevel
        
        return output
        