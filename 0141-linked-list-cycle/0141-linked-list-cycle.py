# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pt1,pt2=head,head

        while pt1 and pt1.next and pt2:
            pt1=pt1.next.next
            pt2=pt2.next
            if pt1 == pt2:
                return True
        return False
        