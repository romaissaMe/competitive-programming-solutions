class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        if target == 1:
            return 0
        while target>1:
            if target %2 == 0 and maxDoubles>0:
                target=target/2
                maxDoubles-=1
                ans+=1
            elif maxDoubles==0:
                ans+= int(target-1)
                target=1
            else: 
                target-=1
                ans+=1
        
        return ans

        