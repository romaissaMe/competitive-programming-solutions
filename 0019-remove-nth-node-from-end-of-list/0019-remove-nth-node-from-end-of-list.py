# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev=None
        size=0
        #calculate full size
        while curr:
            curr = curr.next
            size+=1
        
        

        curr = head
        for _ in range(size-n):
            prev=curr
            curr = curr.next

        if size-n > 0:
            last=curr.next
            prev.next=last
        else:
            head=head.next

        return head
        