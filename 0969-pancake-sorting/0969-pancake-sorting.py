class Solution:

    def flip(self,arr,k):
        s,e=0,k
        while e>s:
            tmp = arr[s]
            arr[s]=arr[e]
            arr[e]=tmp
            s+=1
            e-=1
        return arr

    def pancakeSort(self, arr: List[int]) -> List[int]:
        if sorted(arr)==arr:
            return []
        
        n = len(arr)
        answer=[]
        for i in range(n):
            mxi = 0
            mxidx=0
            for j in range(0,n-i):
                if arr[j]>mxi:
                    mxi = arr[j]
                    mxidx=j
            
            arr = self.flip(arr,mxidx)  
            arr = self.flip(arr,n-i-1)
            answer.append(mxidx+1)
            answer.append(n-i)
        
        return answer

            

     