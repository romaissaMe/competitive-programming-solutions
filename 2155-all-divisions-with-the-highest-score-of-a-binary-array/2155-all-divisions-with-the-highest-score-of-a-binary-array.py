class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        freqs = {}
        total_ones = len([x for x in nums if x == 1])
        left_side_zeros = 0
        left_side_ones = 0
        freqs[0]=total_ones
        for i in range(1,n+1):
            if nums[i-1]==0:
                left_side_zeros += 1
            else:
                left_side_ones += 1

            right_side_ones = total_ones - left_side_ones
            freqs[i]= right_side_ones + left_side_zeros
        maximum = max(freqs.values())
        result = [index for index in freqs if freqs[index]==maximum]
        return result



        