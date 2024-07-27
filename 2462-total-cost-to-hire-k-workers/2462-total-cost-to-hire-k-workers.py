import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        heap_l, heap_r = [], []
        l, r = 0, n - 1
        
        for i in range(candidates):
            if l <= r:
                heapq.heappush(heap_l, (costs[l], l))
                l += 1
            if r >= l:
                heapq.heappush(heap_r, (costs[r], r))
                r -= 1
        
        ans = 0
        
        for _ in range(k):
            if heap_r and (not heap_l or heap_l[0] > heap_r[0]):
                cost, idx = heapq.heappop(heap_r)
                ans += cost
                if r >= l:
                    heapq.heappush(heap_r, (costs[r], r))
                    r -= 1
            else:
                cost, idx = heapq.heappop(heap_l)
                ans += cost
                if l <= r:
                    heapq.heappush(heap_l, (costs[l], l))
                    l += 1
        
        return ans





