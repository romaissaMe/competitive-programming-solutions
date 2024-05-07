# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        
        overflow=0
        ans=dummy

        while l1 and l2:
            res = l1.val+l2.val+overflow
            overflow=res//10 
            dummy.next = ListNode(res%10)
            dummy = dummy.next
            l1=l1.next
            l2=l2.next
        
        temp= l1 if l1 else l2

        while temp:
            #append node with val =0
            res = temp.val+overflow
            overflow = res//10
            dummy.next = ListNode(res%10)
            dummy = dummy.next
            temp=temp.next

        if overflow >0:
            #add node with value = overflow
            dummy.next = ListNode(overflow)

        return ans.next    