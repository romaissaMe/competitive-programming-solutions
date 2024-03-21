from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_freqs = Counter(p)
        p1=0
        p2=len(p)
        w_freqs= Counter(s[0:p2])
        res=[]
        if w_freqs == p_freqs:
                res.append(p1)
        print(res)
        while p2<len(s) and p1<len(s):
            curr_c = s[p1]
            w_freqs[curr_c] = w_freqs[curr_c]-1 
            if w_freqs[curr_c] == 0:
                del(w_freqs[curr_c])
            last_c = s[p2]
            w_freqs[last_c] = w_freqs.get(last_c,0)+1
            p1+=1
            if w_freqs == p_freqs:
                res.append(p1)
            
            p2+=1
        return res

            

                
            
            





        