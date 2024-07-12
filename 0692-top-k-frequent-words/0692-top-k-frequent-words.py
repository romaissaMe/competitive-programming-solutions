from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frq=defaultdict(int)
        ans=[]

        for w in words :
            frq[w]-=1

       
        li = sorted(frq,key= lambda x : (frq[x],x))[:k]
        return li

