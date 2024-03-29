class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1=0
        p2=0
        count=0
        maxLength=0
        while p2<len(nums):
            if nums[p2]==0:
                count+=1
            if count>1:
                while count>1:
                    if nums[p1]==0:
                        count=count-1
                    p1+=1
            maxLength=max(maxLength,p2-p1)
            p2+=1
        return maxLength

                


