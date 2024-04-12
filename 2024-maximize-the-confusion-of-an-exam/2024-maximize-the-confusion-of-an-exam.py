class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        s,e=0,0
        n= len(answerKey)
        maxlength=0
        cntF,cntT =0,0
        while e<n:
            if answerKey[e]=="T":
                cntT+=1
            else:
                cntF+=1
            
            while min(cntT,cntF)>k :
                if answerKey[s]=="F":
                    cntF-=1
                else:
                    cntT-=1
                s+=1
            maxlength=max(maxlength,e-s+1)
            e+=1
        
        return maxlength

