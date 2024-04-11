class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l,r=0,0
        maxlength=0
        while r<len(nums):
            while k == 0 and nums[r]==0:
                if nums[l]==0:
                    k+=1
                l+=1
            if nums[r]==0:
                k-=1
            maxlength=max(maxlength,r-l+1)
            r+=1

           
        return maxlength

