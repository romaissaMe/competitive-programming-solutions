# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def reverseList(self,head):
        nodes=[]
        while head:
            nodes.append(head)
            head=head.next
        nodes.reverse()
        for i in range(len(nodes)-1):
            nodes[i].next=nodes[i+1]
        nodes[-1].next=None
        return nodes[0]

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ans= dummy
        stack1=[]
        stack2=[]
        overflow,res =0,0

        while l1 and l2:
            stack1.append(l1)
            stack2.append(l2)
            l1=l1.next
            l2=l2.next
        
        while l1:
            stack1.append(l1)
            l1=l1.next
        while l2:
            stack2.append(l2)
            l2=l2.next

        while len(stack1)>0 and len(stack2)>0:
            res = stack1.pop().val+stack2.pop().val+overflow
            overflow=res//10 
            dummy.next = ListNode(res%10)
            dummy = dummy.next
            
        temp=[]
        if len(stack1)>0:
            temp= stack1
        elif len(stack2)>0:
            temp=stack2
        while len(temp)>0:
            res = temp.pop().val+overflow
            overflow = res//10
            dummy.next = ListNode(res%10)
            dummy = dummy.next
           

        if overflow >0:
            #add node with value = overflow
            dummy.next = ListNode(overflow)
        
      
        
        return self.reverseList(ans.next)


        

        