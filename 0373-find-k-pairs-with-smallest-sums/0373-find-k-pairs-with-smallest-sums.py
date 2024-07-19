import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans=[]
        heap_1,heap_2=[],[]

        for x,y in zip(nums1,nums2):
            heapq.heappush(heap_1,x)
            heapq.heappush(heap_2,y)
        
        for _ in range(k):
            if heap_1[0]<heap_2[0]:
                e = heapq.heappop(heap_2)
                ans.append([heap_1[0],e])
            else:
                e = heapq.heappop(heap_1)
                ans.append([heap_2[0],e])
        
        return ans
                
