class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        
        if rowIndex==1:
            return [1,1]
        
        else:
            res = self.getRow(rowIndex-1)
            ans = [1]*(rowIndex+1)
            for i in range(1,rowIndex):
                ans[i]=res[i-1]+res[i]
            return ans
        
        