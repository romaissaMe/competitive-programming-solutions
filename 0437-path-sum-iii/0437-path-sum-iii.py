# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node,sum_):

            nonlocal ans

            if node == None:
                return 


            if sum_ + node.val == targetSum:
                ans+= 1

            

            dfs(node.left,sum_ + node.val) 
            dfs(node.right,sum_+ node.val)
            dfs(node.left,0) 
            dfs(node.right,0) 
        
        ans = 0
        dfs(root,0)

        return ans
            




        