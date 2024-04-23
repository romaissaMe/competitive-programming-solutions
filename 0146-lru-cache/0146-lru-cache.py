class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
       
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def move_to_front(self, node):
       
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
       
        tail = self.tail.prev
        self.remove_node(tail)
        return tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_front(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            
            node = self.cache[key]
            node.value = value
            self.move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used node
                tail = self.pop_tail()
                del self.cache[tail.key]
            # Add new key-value pair
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self.add_node(new_node)
