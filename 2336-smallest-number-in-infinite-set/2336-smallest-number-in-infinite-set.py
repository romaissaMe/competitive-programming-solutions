import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.outset=set()
        self.heap = list(range(1,1001))
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        x = heapq.heappop(self.heap)
        self.outset.add(x)
        return x

    def addBack(self, num: int) -> None:
        if num in self.outset:
            self.outset.remove(num)
            heapq.heappush(self.heap,num)
       

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)