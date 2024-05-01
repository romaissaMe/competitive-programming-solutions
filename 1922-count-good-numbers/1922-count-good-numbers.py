class Solution:

    def pow(self,x,n):    
        temp=0
        if n ==0:
            return 1
        temp = self.pow(x,int(n/2)) 

        if n%2==0:
            return (temp*temp) % (10**9 +7)
        else:
            if n<0:
                return ((temp*temp)/x) % (10**9 +7)
            else:
                return (x*temp*temp) % (10**9 +7)


    def countGoodNumbers(self, n: int) -> int:
        odd = n//2
        even = odd + n%2  #because we consider and start from  index 0 as even
        return (self.pow(4,odd) *  self.pow(5,even)) % (10**9 +7) 
        

