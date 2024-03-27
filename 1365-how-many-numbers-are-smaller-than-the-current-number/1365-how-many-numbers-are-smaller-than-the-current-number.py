class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = [0] * 101  # Initialize an array to store counts of numbers from 0 to 100
        for num in nums:
            counts[num] += 1 
        
        # Calculate the prefix sum of counts to get the number of smaller elements
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]
        
        result = [counts[num - 1] if num != 0 else 0 for num in nums]
        
        return result