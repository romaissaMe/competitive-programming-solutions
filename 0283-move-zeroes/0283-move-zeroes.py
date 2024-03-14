class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        n = len(nums)
        while p1 <n and p2<n:
            if nums[p2]==0:
                if nums[p1]!=0:
                    nums[p2],nums[p1]=nums[p1],nums[p2]
                    p2+=1
                else:
                    p1+=1
            else:
                p1+=1
                p2+=1
        return nums