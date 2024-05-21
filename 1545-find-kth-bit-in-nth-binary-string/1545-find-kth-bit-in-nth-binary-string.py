class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s=""
        def reverse_invert(binary_str):
            reversed_str = binary_str[::-1]
            inverted_str = ''.join('1' if digit == '0' else '0' for digit in reversed_str)
            return inverted_str
    
        def findstr(n):
            if n==1:
                return  "0"
            else:
                x= findstr(n-1)
                return x+"1"+reverse_invert(x)

        
        s= findstr(n)
        print(s)
        return s[k-1]
        

         