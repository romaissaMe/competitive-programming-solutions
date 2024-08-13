class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        n=len(nums)

        def solve(index):

            if index>=n-2:
                return nums[index]
                
            if index in memo:
                return memo[index]
            
            ans =0
            for i in range(index+2,n):
                res = nums[index]+solve(i)
                ans = max(ans,res)
            
            memo[index]=ans
            return ans

        ans = max(solve(i) for i in range(n))
        return ans
            

        