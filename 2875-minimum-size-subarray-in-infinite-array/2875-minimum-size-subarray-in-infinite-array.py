class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        win_size, target = divmod(target, sum(nums))

        if target == 0: return n * win_size

        res = float("inf")
        prefix = {0 : -1} 
        running_sum = 0
        for i, n in enumerate(nums * 2):
            running_sum += n
            need = running_sum - target
            if need in prefix:
                res = min(res, i - prefix[need])
            prefix[running_sum] = i
        return -1 if res == float("inf") else n * win_size + res
        



        