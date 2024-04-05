class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = 'aeiou'
        res = []
        n = len(words)
        correct_words = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]
        for i in range(1,n):
            correct_words[i]+=correct_words[i-1]
        
        for q in queries:
            s,e = q
            nb = correct_words[e]-correct_words[s-1] if s>0 else correct_words[e]
            res.append(nb)

        return  res

