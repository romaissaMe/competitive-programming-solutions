class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def isNice(subs: str) -> bool:
            chars = set(subs)
            for c in chars:
                if (c.swapcase() not in chars):
                    return False
            return True
        
        def helper(s: str) -> str:
            if isNice(s):
                return s
            
            max_len = 0
            result = ""
            for i in range(len(s)):
                if s[i].swapcase() not in s:
                    left = helper(s[:i])
                    right = helper(s[i+1:])
                    
                    if len(left) > max_len:
                        max_len = len(left)
                        result = left
                    if len(right) > max_len:
                        max_len = len(right)
                        result = right
                    break
            
            return result
        
        return helper(s)