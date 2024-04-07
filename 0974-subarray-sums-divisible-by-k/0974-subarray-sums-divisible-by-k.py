class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        pref= 0
        count = [1] + [0] * k
        for n in nums:
            pref = (pref + n) % k
            res += count[pref]
            count[pref] += 1
        return res