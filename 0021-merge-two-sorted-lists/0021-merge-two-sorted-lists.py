# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create first Node
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
            merged = ListNode(list2.val,None)
            list2 = list2.next
            
        else:
            merged = ListNode(list1.val,None)
            list1 = list1.next
            
        
        
        curr = merged
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = ListNode(list2.val,None)
                list2 = list2.next
                
            else:
                curr.next = ListNode(list1.val,None)
                list1 = list1.next
           
            curr = curr.next
        
        curr.next = list1 if list1 else list2
        
        return merged