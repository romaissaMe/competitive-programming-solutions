class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.pref = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.pref[i] = self.pref[i - 1] + nums[i - 1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.pref[right + 1] - self.pref[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)