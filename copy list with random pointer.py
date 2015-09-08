# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        current = head
        while current:
            next = current.next
            new_node = RandomListNode(current.label)
            new_node.next = next
            current.next = new_node
            current = next
        
        current = head
        while current:
            current.next.random = None if not current.random else current.random.next
            current = current.next.next
        
        new_head = head.next
        current,new_current = head,new_head
        while current:
            next = new_current.next
            if next:
                new_current.next = next.next
            current.next = next
            current,new_current = next,new_current.next
        return new_head
        