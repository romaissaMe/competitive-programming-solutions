from collections import defaultdict
from collections import Counter
class Solution(object):
     # Check if str2 contains at least as many occurrences of each character in str1
    def check_sim(self, count_str1, count_str2):
        for char, count in count_str1.items():
            if count_str2.get(char, 0) < count:
                return False
        return True

    def minWindow(self, s, t):
        l, r = 0, 0
        cnt = defaultdict(int)
        bs = Counter(t)
        min_size = float('inf')
        res = ""

        while r < len(s):
            cnt[s[r]] += 1  

            while self.check_sim(bs, cnt) and l <= r:
                window_size = r - l + 1
                if window_size < min_size:
                    min_size = window_size
                    res = s[l:r+1]

                cnt[s[l]] -= 1
                l += 1

            r += 1 

        return res
            



        