class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freqs={}
        word = list(s)
        for i,x in enumerate(s):
            freqs[x]=freqs.get(x,0)+1
        indexes= [word.index(x) for x, freq in freqs.items() if freq==1]
        if len(indexes)>0:
            return min(indexes)
        else:       
            return -1

        