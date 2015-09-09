from collections import deque
class MaxQueue(object):
    def __init__(self):
        self.q = deque()
        self.max_q = deque()
    def put(self,val):
        self.q.append(val)
        while self.max_q and self.max_q[-1] < val:
            self.max_q.pop()
        self.max_q.append(val)
    def get(self):
        if self.q[0] == self.max_q[0]:
            self.max_q.popleft()
        return self.q.popleft()
    def max(self):
        return self.max_q[0]

class Solution(object):    
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        q = MaxQueue()
        for num in nums[:k]:
            q.put(num)
        res = [q.max()]
        for i in xrange(k,len(nums)):
            q.get()
            q.put(nums[i])
            res.append(q.max())
        return res
    