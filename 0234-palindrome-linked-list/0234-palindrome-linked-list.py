# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        tmp=[]
        size = 0
        curr = head
        while curr:
            tmp.append(curr.val)
            curr=curr.next
            size+=1

        i,j=0,size-1
        while i < j:
            if tmp[i]!=tmp[j]:
                return False
            i+=1
            j-=1

        return True
            