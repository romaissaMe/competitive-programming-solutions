import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream=[]
        self.k=k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        if len(self.stream) > self.k:
            heapq.heappop(self.stream)
        return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)