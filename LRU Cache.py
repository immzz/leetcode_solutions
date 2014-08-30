class Node:
    # @param key, int
    # @param value, int
    # @param next, Node
    # @param prev, Node
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
 
# Used a doubly linked list and a hash
class LRUCache:
 
    # @param capacity, an integer
    def __init__(self, capacity):
        self.count = 0 # number of elements already stored
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.hash = {}
        
 
    # @return an integer; -1 means not found
    def get(self, key):
        if key in self.hash:
            node = self.hash[key]
            self.update_position(node)
            return node.value
        else:
            return -1
        
 
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        #Update node content
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            self.update_position(node)
            return
                
        if self.count == self.capacity: #Purge the cache if necessary
            stale_key = self.tail.key
            del self.hash[stale_key]
            node = self.tail
            node.key = key
            node.value = value
        else:
            node = Node(key, value, None, self.tail)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            
            self.count += 1
        
        self.hash[key] = node
        self.update_position(node)
 
    
    # Advance a node to head of linked list
    def update_position(self, node):
        if self.head == node:
            return
        
        prev = node.prev
        next = node.next
        prev.next = next
        if next is not None:
            next.prev = prev
        else:
            self.tail = prev
        
        head = self.head
        head.prev = node
        self.head = node
        node.next = head
        node.prev = None