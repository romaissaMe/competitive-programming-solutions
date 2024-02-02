class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ''
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            output += word1[i] + word2[i]
        output += word1[min_len:] + word2[min_len:]
        return output       