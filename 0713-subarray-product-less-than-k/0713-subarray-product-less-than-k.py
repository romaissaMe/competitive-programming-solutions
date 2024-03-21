import numpy as np
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        count = 0
        product = 1
        p1 = 0
        
        for p2, num in enumerate(nums):
            product *= num
            
            while product >= k:
                product /= nums[p1]
                p1 += 1
            
            count += p2 - p1 + 1
        
        return count

        