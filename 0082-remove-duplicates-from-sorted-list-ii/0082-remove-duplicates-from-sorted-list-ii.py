# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        delete = True
        dummy=ListNode(0)
        dummy.next=head
        prev = dummy
        curr = head
        red=None
        while curr and curr.next:
            if curr.val == curr.next.val or curr.val ==red:
                if curr.val ==red:
                    prev.next = curr.next
                else: 
                    prev.next = curr.next.next
                red = curr.val
                curr = prev.next
                

            else:
                prev = curr
                curr=curr.next
        
        #handle last node
        if curr and curr.val == red:
            prev.next = None
        
        return dummy.next
                

        