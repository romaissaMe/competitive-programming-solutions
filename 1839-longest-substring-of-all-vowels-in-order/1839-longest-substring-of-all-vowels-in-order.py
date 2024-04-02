class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        window_size = 0
        vowels = set('aeiou')
        l=r = 0
        while r < n:
            substring = [word[r]]
            l=r
            r += 1  
            while r < n and word[r] >= substring[-1] and word[l]=="a":
                substring.append(word[r])
                r += 1
                
            if set(substring) == vowels:
                window_size = max(window_size, len(substring))
            
          
            
        return window_size





        