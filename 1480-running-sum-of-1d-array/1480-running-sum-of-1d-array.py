class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)>0:
            res=[nums[0]]
            for i in range(1,len(nums)):
                res.append(res[i-1]+nums[i])
        else:
             return []
        
        return res
        