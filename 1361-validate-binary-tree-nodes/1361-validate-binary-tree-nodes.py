from collections import defaultdict
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents= defaultdict(set)
        haseCycle=False
        
        for i in range(n):
            if leftChild[i]!=-1:
                parents[leftChild[i]].add(i)
            if rightChild[i]!=-1:
                parents[rightChild[i]].add(i)
        
        if len(parents.keys())==n:
            return False
        
        for i in range(n):
            if i not in parents.keys():
                root = i
                break
        
        def dfs(node,visited):

            if node == -1:
                return True
            
           
            if node not in visited:
                visited.add(node)
                return dfs(leftChild[node],visited) and dfs(rightChild[node],visited)
                
            else:
                return False
        
        visited = set()
        return  dfs(root,visited) and len(visited)==n
      
            
        