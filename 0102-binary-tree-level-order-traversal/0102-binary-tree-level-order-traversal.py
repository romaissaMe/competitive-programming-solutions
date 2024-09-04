from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = Queue()
        ans = []

        if root:
            q.put(root)
     
    
        while not q.empty():

            c = []
            
            for _ in range(q.qsize()):
                node = q.get()
                c.append(node.val)

                if node.left:
                    q.put(node.left)

                if node.right:
                    q.put(node.right)
            
            
            if c:
                ans.append(c)
                

        return ans


        