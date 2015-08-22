# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    
    # corner case: [[],[1]]
    def mergeKLists(self, lists):
            if not lists:
                return None
            if len(lists) == 1:
                return lists[0]
            mid = (len(lists)-1)/2
            left = self.mergeKLists(lists[0:mid+1])
            right = self.mergeKLists(lists[mid+1:])
            return self.merge2Lists(left,right)
        
        def merge2Lists(self,list1,list2):
            dummy = ListNode(None)
            current = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            current.next = list1 if list1 else list2
            return dummy.next