class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def solve(index):
            if index in memo:
                return memo[index]

            if index >= n:
                return 0
            
            ans = 1  # the element itself
            for i in range(index + 1, n):
                if nums[index] < nums[i]:
                    ans = max(ans, 1 + solve(i))

            memo[index] = ans
            return memo[index]

        ans = max(solve(i) for i in range(n))
        return ans
