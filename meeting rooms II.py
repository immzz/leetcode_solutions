# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from heapq import *
class Solution:
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        h = []
        min = 0
        intervals.sort(key = lambda x:x.start)
        for i in intervals:
            while h and h[0] <= i.start:
                heappop(h)
            heappush(h,i.end)
            min = max(min,len(h))
        return min