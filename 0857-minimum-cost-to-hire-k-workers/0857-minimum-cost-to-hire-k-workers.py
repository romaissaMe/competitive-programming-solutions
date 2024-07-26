import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(wage)
        
        workers = [(wage[i] / quality[i], quality[i]) for i in range(n)]
        
        workers.sort()
    
        maxHeap = []
        sumHeap = 0
        
        for i in range(k):
            heapq.heappush(maxHeap, -workers[i][1])
            sumHeap += workers[i][1]
        
        captainRatio = workers[k-1][0]
        minCost = captainRatio * sumHeap
        
       
        for captain in range(k, n):
            captainRatio = workers[captain][0]
            
            if workers[captain][1] < -maxHeap[0]:
                sumHeap += workers[captain][1] + heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, -workers[captain][1])
                
                cost = captainRatio * sumHeap
                minCost = min(minCost, cost)
        
        return minCost
