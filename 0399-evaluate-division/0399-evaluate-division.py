from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda: defaultdict(lambda:-1))
        res= []

        def dfs(node,dest,weight,visited):
            if node == dest:
                return weight
            
            visited.add(node)
            for c,w in graph[node].items():
                if c in visited:
                    continue
                result= dfs(c,dest,weight*w,visited)
                if result>-1:
                    return result

            return -1

        for e,val in zip(equations,values):
            x,y = e
            graph[x][y]=val
            graph[y][x]=1/val


        for x,y in queries:
            if x not in graph or y not in graph : res.append(-1)
            elif x==y: res.append(1)
            else: res.append(dfs(x,y,1,set()))


        return res