# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, current_sum):
            nonlocal ans
            if not node:
                return
       
            current_sum = current_sum * 10 + node.val
            
            if not node.left and not node.right:
                ans += current_sum
                return

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        
        dfs(root, 0)
        return ans
            
        