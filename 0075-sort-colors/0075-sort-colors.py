class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        for i in range(length):
            for j in range(length-i-1):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                
        return nums