from collections import defaultdict
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        n = len(nums)
        d = defaultdict(int)

        while p <n:
            if d[nums[p]] == 2:
                if p < n-1:
                    for i in range(p,n-1):
                        nums[i] = nums[i+1]
                    n-=1
                
                else:
                    return p
            else:
                d[nums[p]]+=1
                p+=1
        
        return p

        