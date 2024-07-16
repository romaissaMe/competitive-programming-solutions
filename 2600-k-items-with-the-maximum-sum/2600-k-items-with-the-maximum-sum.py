class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        sum_ = 0
        if k-numOnes>0:
            sum_+=numOnes
            k-=numOnes
            if k-numZeros>0:
                k-=numZeros
                sum_+=k*(-1)
            else:
                return sum_

        else:
            return sum_+k
        
        return sum_

        