# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

linked_list = LinkedList(head)
linked_list.printlist()
linked_list.getAt(4)
linked_list.printlist()
linked_list.insertAt(4,0)
linked_list.printlist()
linked_list.delAt(4)
linked_list.printlist()
linked_list.delAt(3)
linked_list.printlist()
linked_list.delAt(0)
linked_list.printlist()
print linked_list.searchAt(1)
print linked_list.searchAt(4)