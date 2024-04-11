from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        :type fruits: List[int]
        :rtype: int
        """
        maxlength=0
        s,e=0,0
        baskets = defaultdict()
        n = len(fruits)
        while e<n:
            if (fruits[e] not in baskets and len(baskets)<2) or fruits[e] in baskets :
                baskets[fruits[e]]=e
                maxlength= max(maxlength,e-s+1)
                e+=1
            
            else:
                x = min(baskets.values())
                s=x+1
                fruit = [f for f in baskets.keys() if baskets[f]==x]
                del(baskets[fruit[0]])

            
        return maxlength