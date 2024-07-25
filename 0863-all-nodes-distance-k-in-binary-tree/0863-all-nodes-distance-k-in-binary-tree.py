from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans=[]
        parents= defaultdict(TreeNode)
                
        def track_parents(node,par):
            if not node: return 

            parents[node.val]=par
            track_parents(node.left,node)
            track_parents(node.right,node)
            

        def bfs(root,visited):
            q=Queue()
            q.put((0,root))  
            visited.add(root.val)          
            while not q.empty():
                level,node=q.get()

                if level==k: 
                    ans.append(node.val)
                
                elif level < k:
                    if node.left and node.left.val not in visited:
                        visited.add(node.left.val)
                        q.put((level + 1, node.left))
                    if node.right and node.right.val not in visited:
                        visited.add(node.right.val)
                        q.put((level + 1, node.right))
                    if parents[node.val] and parents[node.val].val not in visited:
                        visited.add(parents[node.val].val)
                        q.put((level + 1, parents[node.val]))


        track_parents(root,None)  
        bfs(target,set())
        return ans
