class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        n = len(trips)
        pref_sum = [0]*1000
        for p,s,e in trips:
            pref_sum[s]+=p
            if e+1<n:
                pref_sum[e+1]-=p
        
        for i in range(1,1000):
            pref_sum[i]+=pref_sum[i-1]
        
        for c in pref_sum:
            if c>capacity:
                return False
        
        return True