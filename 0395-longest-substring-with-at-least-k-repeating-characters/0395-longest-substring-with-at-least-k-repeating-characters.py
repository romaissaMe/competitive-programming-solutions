class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = Counter(s)
        n = len(s)
        elems = len(freq)
        ans = 0

        for i in range(1,elems+1):
            counter = defaultdict(int)
            l=0
            for r in range(n):
                counter[s[r]]+=1
                while len(counter) > i:
                    counter[s[l]]-=1
                    if counter[s[l]] == 0:
                        del counter[s[l]] 
                    l+=1
                if all(f >= k for f in counter.values()):
                    ans= max(ans,r-l+1)
        
        return ans
            
            

                







        