class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
    
        for num in nums:
            # Add to ones if it's not in twos
            ones = (ones ^ num) & ~twos
            
            # Add to twos if it's not in ones
            twos = (twos ^ num) & ~ones
            
        return ones