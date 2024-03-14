class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n_equal_target=0
        n_small=0
        result = []
        for e in nums:
            if e == target:
                n_equal_target+=1
            elif e< target:
                n_small+=1
        if n_equal_target != 0:
            result.append(n_small)
            for i in range(1,n_equal_target):
                result.append(n_small+i)

        return result
        

        