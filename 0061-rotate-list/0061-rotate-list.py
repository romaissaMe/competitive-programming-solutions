# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left,right=head,head
        prev=None
        size=0

        if k==0 or not head or not head.next:
            return head
        #get size
        while right:
            size+=1
            prev=right
            right=right.next

        if k>size:
            k=k%size
            if k==0:
                return head
        elif k == size:
            return head

        for _ in range(size-k):
            prevleft=left
            left=left.next
        
        prev.next=head
        head=left
        prevleft.next=None
        
        return head

      

            


        

         

        

        
           
            