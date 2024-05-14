class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high=len(nums)-1
        low=0
        while low<high:
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low=mid+1
            else: 
                high = mid
        
        return (high+1) if target >nums[high] else high