class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}

        def solve(idx1, idx2):

            if idx2 == len(t):
                return 1

            if idx1 == len(s):
                return 0

            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            include = 0
            exclude = 0
            if s[idx1] == t[idx2]:
                include = solve(idx1 + 1, idx2 + 1)
                exclude = solve(idx1 + 1, idx2)
                res = include + exclude
            else:
                res = solve(idx1 + 1, idx2)
            
            memo[(idx1, idx2)] = res

            return res
        

        
        ans = solve(0,0)
        return ans

