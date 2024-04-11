class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        s,e=0,n-k
        subsum=float('inf')
        prefsum=[0]*(n+1)
        for i in range(1,n+1):
            prefsum[i]=prefsum[i-1]+cardPoints[i-1]
        totalsum=prefsum[-1]
        while e<n+1:
            subsum=min(subsum,prefsum[e]-prefsum[s])
            print(subsum)
            e+=1
            s+=1
        
        return totalsum-subsum

