# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d=0
        def visit(node,d):
            if node:
                d+=1
                d=max(visit(node.left,d),visit(node.right,d))
                return d
                
            return d
    
        return visit(root,d)