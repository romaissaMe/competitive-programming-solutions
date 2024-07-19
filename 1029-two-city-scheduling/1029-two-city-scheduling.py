import heapq
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        li=[]
        n = len(costs)
        ans=0
        for i,x in enumerate(costs):
            heapq.heappush(li,(-(x[1]-x[0]),i))
        i=0

        while i<n:
            _,index= heapq.heappop(li)
            if i<n/2:
                ans+=costs[index][0]
            else:
                ans+=costs[index][1]
            i+=1
        return ans


        