class Solution:
    def longestPalindrome(self, s: str) -> str:
           
            n=len(s)
            dp = [[False] * (n+1) for i in range(n+1)]
            lps = 1
            ans=""

            for i in range(n):
                dp[i][i]= True
                
            
            for i in range(1,n):
                for j in range(i):

                    if s[i] != s[j]:
                        continue
                    
                    if i-j == 1 or dp[i-1][j+1]:           
                        dp[i][j]= True

                        if i-j+1 >= lps:
                            ans = s[j:i+1]
                            lps = i-j+1

                       
            
            return ans
       
            
            
        