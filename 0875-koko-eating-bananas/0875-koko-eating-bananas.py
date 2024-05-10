class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def good(n):
            cnt=0
            for i in piles:
                cnt+=math.ceil(i/n)
            return cnt<=h

        high = max(piles)
        low=1
000000111
        while low<high:
            mid = (high+low)//2
            if good(mid):
                high = mid
            else:
                low=mid+1
        
        return high

