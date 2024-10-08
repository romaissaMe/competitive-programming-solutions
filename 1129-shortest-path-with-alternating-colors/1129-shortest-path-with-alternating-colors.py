from queue import Queue
from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q = Queue()
        graph = defaultdict(list)
        ans = [float('inf')]*n
        ans[0]=0
        visited = set()

        for node, child in redEdges:
            graph[node].append((child,"r"))

        for node, child in blueEdges:
            graph[node].append((child,"b"))
        
        
        q.put((0,None,0))
        
        while not q.empty():
            node,c,l = q.get()
            for child in graph[node]:
                if child[1] != c and (child[0],child[1]) not in visited:
                        q.put((child[0],child[1],l+1))
                        ans[child[0]]=min(ans[child[0]],l+1)       
                        visited.add((child[0],child[1]))

        for i in range(len(ans)):
            if ans[i]==float('inf'):
                ans[i]=-1

        return ans




        