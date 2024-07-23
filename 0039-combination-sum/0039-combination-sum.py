class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        def backtrack(combi, start):
            nonlocal ans
            if sum(combi) == target:
                ans.add(tuple(combi))
                return

            for i in range(start, len(candidates)):
                combi.append(candidates[i])
                if sum(combi) <= target:
                    backtrack(combi, i)  
                combi.pop()
        
        backtrack([], 0)
        return [list(tup) for tup in ans]
