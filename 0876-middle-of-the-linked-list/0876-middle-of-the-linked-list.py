# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fp=head
        sp=head
        while fp:
            if fp.next:
                fp=fp.next.next
                sp=sp.next
            else:
                fp=None
        return sp
        