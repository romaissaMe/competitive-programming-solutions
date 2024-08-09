class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)/2
        memo={}
        n=len(nums)

        def solve(index,sumSub):
            if sumSub==target:
                return True
            if (index, sumSub) in memo:
                return memo[(index, sumSub)]

            if index >= len(nums) or sumSub > target:
                return False

            result= solve(index+1,sumSub) or solve(index+1,sumSub+nums[index])
            memo[(index, sumSub)] = result
            return result

            
        return solve(0,0)