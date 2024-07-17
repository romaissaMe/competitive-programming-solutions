class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        k = len(nums)


        def backtrack(sol):
            if len(sol)==k:
                res.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack(sol)
                    sol.pop()
            return res
        
        return backtrack([])
        

                