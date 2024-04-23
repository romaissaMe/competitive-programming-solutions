# Definition for a Node.

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_map = {}
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        # Update next and random pointers of copied nodes
        current = head
        while current:
            copied_node = node_map[current]
            if current.next:
                copied_node.next = node_map[current.next]
            if current.random:
                copied_node.random = node_map[current.random]
            current = current.next
        
        return node_map[head]


        






