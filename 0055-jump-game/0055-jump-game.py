class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums)-1
        i=end-1

        while end>0 and i>=0:
            if nums[i]>=end-i:
                end=i
                i-=1
            else:
                i-=1
        
        return end==0
            
            
        