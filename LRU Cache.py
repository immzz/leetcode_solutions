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
            self._append(current_node)
            return current_node.val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            self._remove(self.dic[key])
            self._append(ListNode(value,key))
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
            #print "remove tail"
            self.tail = current_node.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            current_node.next = current_node.prev = None
            del self.dic[current_node.key]
            return
        if current_node == self.head:
            self.head = current_node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            current_node.prev = current_node.next = None
            del self.dic[current_node.key]
            return
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        current_node.prev = current_node.next = None
        del self.dic[current_node.key]
        

        
def print_list(head):
    a = []
    while head:
        print str(head.key)+","+str(head.val),
        head = head.next
    print
'''
cache = LRUCache(2)
cache.set(2,1)
print_list(cache.head)
cache.set(1,1)
print_list(cache.head)
cache.set(2,3)
print_list(cache.head)
cache.set(4,1)
print_list(cache.head)
cache.get(1)
print_list(cache.head)
cache.get(2)
print_list(cache.head)
'''
cache = LRUCache(10)
cache.set(10,13)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.set(3,17)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.set(6,11)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.set(10,5)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.set(9,10)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.get(13)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.set(2,19)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.get(2)
cache.get(3)
cache.set(5,25)
cache.get(8)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.set(9,22)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.set(5,5)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.set(1,30)
print_list(cache.head)
print cache.dic.keys()
print '---------'
print cache.tail.key
cache.get(11)
print_list(cache.head)
print cache.dic.keys()
print '---------+'
print cache.tail.key,cache.tail.prev.key
cache.set(9,12)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.get(7)
cache.get(5)
cache.get(8)
cache.get(9)
cache.set(4,30)
cache.set(9,3)
cache.get(9)
cache.get(10)
cache.get(10)
cache.set(6,14)
cache.set(3,1)
cache.get(3)
cache.set(10,11)
cache.get(8)
cache.set(2,14)
cache.get(1)
cache.get(5)
cache.get(4)
cache.set(11,4)
cache.set(12,24)
cache.set(5,18)
cache.get(13)
cache.set(7,23)
cache.get(8)
cache.get(12)
cache.set(3,27)
cache.set(2,12)
cache.get(5)
cache.set(2,9)
cache.set(13,4)
cache.set(8,18)
cache.set(1,7)
cache.get(6)
cache.set(9,29)
cache.set(8,21)
cache.get(5)
cache.set(6,30)
cache.set(1,12)
print_list(cache.head)
cache.get(10)
cache.set(4,15)
cache.set(7,22)
cache.set(11,26)
cache.set(8,17)
cache.set(9,29)
cache.get(5)
cache.set(3,4)
cache.set(11,30)
cache.get(12)
cache.set(4,29)
cache.get(3)
cache.get(9)
cache.get(6)
cache.set(3,4)
cache.get(1)
cache.get(10)
cache.set(3,29)
cache.set(10,28)
cache.set(1,20)
cache.set(11,13)
cache.get(3)
cache.set(3,12)
cache.set(3,8)
cache.set(10,9)
cache.set(3,26)
cache.get(8)
cache.get(7)
cache.get(5)
cache.set(13,17)
cache.set(2,27)
cache.set(11,15)
cache.get(12)
cache.set(9,19)
cache.set(2,15)
cache.set(3,16)
cache.get(1)
cache.set(12,17)
cache.set(9,1)
print_list(cache.head)
print cache.dic.keys()
print '---------'
cache.set(6,19)
cache.get(4)
cache.get(5)
cache.get(5)
cache.set(8,1)
cache.set(11,7)
cache.set(5,2)
cache.set(9,28)
print_list(cache.head)
cache.get(1)#,set(2,2),set(7,4),set(4,22),set(7,24),set(9,26),set(13,28),set(11,26)])



'''
cache.set(1,1)
cache.set(2,2)
cache.set(3,3)
print_list(cache.head)
cache.set(4,4)
print_list(cache.head)
#print cache.dummy
#print cache.dic[3],cache.head,cache.head.next,cache.head.prev
cache.get(3)
#cache.get(3)
#print '-',cache.dummy,cache.tail,cache.dummy.next
#print cache.dic[3],cache.head,cache.head.next,cache.head.next.next
print_list(cache.head)
cache.set(4,4)
print_list(cache.head)
cache.get(2)
print_list(cache.head)
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
'''