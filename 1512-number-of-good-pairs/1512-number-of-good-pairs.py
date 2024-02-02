from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not (1 <= len(nums) <= 100 and all(1 <= num <= 100 for num in nums)):
            print("Review the array's length or the range of its elements")
            return
        output=0
        frequency={}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        for val in frequency.values():
            if val>1:
                output+= (val * (val - 1)) // 2
        return output
  


        