class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i = len(nums)-2
        j = 0
        while i>=0:
            if nums[i]<nums[i+1]:
                break
            i=i-1       
   
        if (i < 0):
            nums.reverse()

        else:
            for j in range(n-1, i, -1):
                if (nums[j] > nums[i]):
                    break

            nums[i], nums[j] = nums[j], nums[i]

            strt, end = i+1, len(nums)

            nums[strt:end] = nums[strt:end][::-1]

        return nums

 




