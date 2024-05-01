class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp=0
        if n ==0:
            return 1
        temp = self.myPow(x,int(n/2))
        if n%2==0:
            return temp*temp
        else:
            if n<0:
                return (temp*temp)/x
            else:
                return x*temp*temp
        