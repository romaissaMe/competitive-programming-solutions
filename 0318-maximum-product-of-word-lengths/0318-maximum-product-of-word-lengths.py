class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bin_ = [0] * len(words)
        ans = 0

        for i,word in enumerate(words):
            for c in word:
                bin_[i] = bin_[i] | 1<<(ord(c)-ord('a'))
        
        for i in range(len(words)):
            for j in range(0,i):
                if bin_[i] & bin_[j] == 0:
                    ans = max(len(words[i])*len(words[j]),ans)
        
        return ans