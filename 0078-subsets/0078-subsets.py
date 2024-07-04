class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        n = len(nums)

        for num in nums:
            sub = []
            for curr in ans:
                sub.append(curr + [num])
            ans.extend(sub)
                
       
        return ans