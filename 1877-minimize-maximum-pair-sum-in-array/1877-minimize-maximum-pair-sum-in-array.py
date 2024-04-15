class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        
        max_pair_sum = float('-inf')
        
        while left < right:
            # Calculate pair sum
            pair_sum = nums[left] + nums[right]
            
            # Update max_pair_sum
            max_pair_sum = max(max_pair_sum, pair_sum)
            
            left += 1
            right -= 1
        
        return max_pair_sum

        