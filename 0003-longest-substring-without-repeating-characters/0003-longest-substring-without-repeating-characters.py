class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1,p2 =0,0
        n = len(s)
        window = set()
        max_length =0
        while p2<n:
            if s[p2] not in window:
                window.add(s[p2])
                max_length = max(max_length,p2-p1+1)
                p2+=1
            else:
                window.remove(s[p1])
                p1+=1
            
            
        
        return max_length
                

            

        