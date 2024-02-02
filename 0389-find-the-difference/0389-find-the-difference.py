class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0

        for char in s + t:
            result ^= ord(char)

        return chr(result)
                
            
         