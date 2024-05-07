from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q= deque()
        max_q = deque()
        n = len(nums)
        max_size=0
        l=0

        for i in range(n):
            while max_q and nums[max_q[-1]]<nums[i]:
                max_q.pop()
            
            max_q.append(i)
            
            while min_q and nums[min_q[-1]] > nums[i]:
                min_q.pop()
            
            min_q.append(i)

            while nums[max_q[0]]-nums[min_q[0]]>limit:
                if max_q[0] == l:
                    max_q.popleft()
                if min_q[0]==l:
                    min_q.popleft()
                l+=1

            max_size = max(max_size,i-l+1)

        return max_size
