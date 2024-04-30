class Solution:
    
    def reverse(self, s: List[str], left: int, right: int) -> None:
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        self.reverse(s, left + 1, right - 1)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)