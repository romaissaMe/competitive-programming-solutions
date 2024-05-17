class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def can_ship(weight):
            r=0
            sum_=0
            d=1
            while r<n:
                sum_+=weights[r]
                if sum_>weight:
                    d+=1
                    sum_=weights[r]
                r+=1
            return d<=days
                
        ans=0
        low = max(weights)
        high = sum(weights)

        while low<=high:
            mid = (low+high)//2
            if can_ship(mid):
                ans=mid
                high=mid-1
            else:
                low = mid+1

        return ans
