class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        max_ = 0
        ans=0
        i=0
        while max_<n:
            if i < len(nums) and max_ +1 >= nums[i]:
                max_ += nums[i]
                i+=1
            
            else:
                ans+=1
                max_ += (max_ + 1)
            
        return ans