class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minlength = float('inf')
        prefsum = [0] * (n + 1)
        
        # Calculate prefix sum array
        for i in range(1, n + 1):
            prefsum[i] = prefsum[i - 1] + nums[i - 1]
        
        s = 0  
        e = 1  
        while e <= n:
            windowsum = prefsum[e] - prefsum[s]
            if windowsum >= target:
                minlength = min(minlength, e - s)
                s += 1
            else:
                e += 1

        if minlength == float('inf'):
            return 0  
        else:
            return minlength

