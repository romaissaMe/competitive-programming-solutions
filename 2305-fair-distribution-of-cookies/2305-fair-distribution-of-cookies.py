class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n= len(cookies)
        ans= float('inf')
        def backtrack(dist,c):
            nonlocal ans
            if c == n:
                ans = min(max(dist),ans)
                return

            for i in range(k):
                dist[i]+=cookies[c]
                backtrack(dist,c+1)
                dist[i]-=cookies[c]
        
        backtrack([0 for i in range(k)],0)

        return ans
            




                
        