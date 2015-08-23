class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        if len(right) >= k:
            return self.findKthLargest(right,k)
        elif len(mid) + len(right) >= k:
            return pivot
        else:
            return self.findKthLargest(left,k-len(mid)-len(right))
        