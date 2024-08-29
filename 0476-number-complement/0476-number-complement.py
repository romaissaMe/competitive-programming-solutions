class Solution:
    def findComplement(self, num: int) -> int:
        
        tmp = num
        cnt = 0
        print(tmp)

        while tmp != 0:
            tmp = tmp >> 1
            cnt+=1
        
        return num ^ ((1 << cnt) -1)