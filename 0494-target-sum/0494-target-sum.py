class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        n=len(nums)
        def solve(index,sum):
            if (index,sum) in memo:
                return memo[(index,sum)]
            if index == n - 1:
              return 1 if sum == target else 0

            res = solve(index+1,sum+nums[index+1]) + solve(index+1,sum-nums[index+1])
            
            memo[(index,sum)]=res
            return res
        

        return solve(-1,0)
            

        