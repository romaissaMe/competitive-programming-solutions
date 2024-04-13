class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:] = list(reversed(nums))
        nums[:k]=list(reversed(nums[:k]))
        nums[k:]=list(reversed(nums[k:]))
        return nums