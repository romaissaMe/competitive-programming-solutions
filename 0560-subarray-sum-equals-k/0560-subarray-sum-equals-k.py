class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = {0: 1}  # Dictionary to store prefix sum frequencies
        current_sum = 0
        
        for num in nums:
            current_sum += num
            count += prefix_sum.get(current_sum - k, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return count
            