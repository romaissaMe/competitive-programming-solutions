class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        n=len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def solve_2(start, end):
            memo = {}
            
            def solve(index):
                if index in memo:
                    return memo[index]

                if index > end:
                    return 0
                
                rob_current = nums[index] + solve(index + 2)
                skip_current = solve(index + 1)
                memo[index] = max(rob_current, skip_current)
                return memo[index]
            
            return solve(start)

        case1 = solve_2(0, n - 2)
        case2 = solve_2(1, n - 1)

        return max(case1, case2)