# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals:
            return intervals
        res = []
        sorted_intervals = sorted(intervals,key=lambda i : i.start)
        current_start = sorted_intervals[0].start
        current_end = sorted_intervals[0].end
        for i in xrange(1,len(sorted_intervals)):
            if sorted_intervals[i].start <= current_end:
                current_end = max(current_end,sorted_intervals[i].end)
            else:
                res.append(Interval(current_start,current_end))
                current_start = sorted_intervals[i].start
                current_end = sorted_intervals[i].end
        res.append(Interval(current_start,current_end))
        return res