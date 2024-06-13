from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        table = defaultdict(int)
        for e in edges:
            for i in e:
                table[i]+=1
        
        _max= max(table.values())
        c = [x for x in table if table[x]==_max]
        return c[0]