class Solution:
    def countSubstrings(self, s: str) -> int:
        memo={}
        def solve(i,j):

            if i == j:
                return 1
           
            if i > j:
                return 0
            
            # Check if the current substring s[i:j+1] is a palindrome
            is_palindrome = (s[i] == s[j]) and (i + 1 > j - 1 or solve(i + 1, j - 1))
            
            current_count = 1 if is_palindrome else 0
            
            res = current_count + solve(i + 1, j) + solve(i, j - 1) - solve(i + 1, j - 1)
            
            return res
            
        return solve(0,len(s)-1)