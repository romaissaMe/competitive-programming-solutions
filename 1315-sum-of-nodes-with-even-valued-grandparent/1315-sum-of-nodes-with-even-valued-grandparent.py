from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def bfs(queue):
            ans=0
            while not queue.empty():
                gd,prt,node= queue.get()

                if gd and gd%2==0:
                    ans+=node.val

                if node.left:
                    queue.put((prt,node.val,node.left))
                if node.right:
                    queue.put((prt,node.val,node.right))
            return ans
            
        que=Queue()
        que.put((None,None,root))
        return bfs(que)


        