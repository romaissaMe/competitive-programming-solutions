import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_piles=[- pile for pile in piles]
        heapq.heapify(max_piles)
        
        for _ in range(k):
            max_val = - heapq.heappop(max_piles)
            heapq.heappush(max_piles,-(max_val-(max_val//2)))

        return - sum(max_piles)