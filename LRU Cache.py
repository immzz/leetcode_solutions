class ListNode(object):
    def __init__(self,val,key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = None
        self.tail = None
        self.dic = {}
        self.capacity = capacity
        
    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dic:
            current_node = self.dic[key]
            self._remove(self.dic[key])
            #print '=',cache.head,cache.head.next,cache.head.prev
            self._append(current_node)
            #print '=',cache.head,cache.head.next,cache.head.prev
            return current_node.val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            self.dic[key].val = value
        else:
            if len(self.dic) == self.capacity:
                self._remove(self.head)
            new_node = ListNode(value,key)
            self._append(new_node)
    def _append(self,node):
        if not self.tail:
            self.tail = self.head = node
        else:
            prev = self.tail
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        self.dic[node.key] = node
    def _remove(self,current_node):
        if current_node == self.tail:
            self.tail = current_node.prev
            if self.tail:
                self.tail.next = None
        key = current_node.key
        del self.dic[key]
        if current_node.prev:
            current_node.prev.next = current_node.next
        else:
            self.head = current_node.next
            self.head.prev = None

        
def print_list(head):
    a = []
    while head:
        a.append(head.val)
        head = head.next
    print " ".join([str(x) for x in a])
cache = LRUCache(2)
cache.set(1,1)
cache.set(2,2)
cache.set(3,3)
print_list(cache.head)
cache.set(4,4)
print cache.dic.keys()
print_list(cache.head)
#print cache.dummy
print cache.dic[3],cache.head,cache.head.next,cache.head.prev
cache.get(3)
#cache.get(3)
#print '-',cache.dummy,cache.tail,cache.dummy.next
print cache.dic[3],cache.head,cache.head.next,cache.head.next.next
print_list(cache.head)
cache.set(4,3)
cache.get(2)
print cache.dic.keys()
cache.set(4,3)
print cache.dic.keys()
cache.set(1,1)
print cache.dic.keys()
print cache.get(2)
print cache.dic.keys()
cache.set(4,1)
print cache.get(1)
print cache.dic.keys()

