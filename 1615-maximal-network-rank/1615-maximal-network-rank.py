from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(set)
        ans = 0

        for a,b in roads:
            graph[a].add(b)
            graph[b].add(a)
        
        for c in range(n):
            deg = len(graph[c])
            for x in range(c+1,n):
                rank = deg + len(graph[x])
                if c in graph[x]:
                    rank-=1
                ans = max(ans,rank)

        return ans

        