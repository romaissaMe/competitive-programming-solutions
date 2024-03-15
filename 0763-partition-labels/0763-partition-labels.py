class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_occurrence = {char: i for i, char in enumerate(s)}
        result = []
        start = end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        
        return result

    

                    
    







            


