class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
        start = nums[0]
        end = nums[0]
        res = []
        for i in xrange(1,len(nums)):
            if nums[i] == end+1:
                end += 1
            else:
                res.append(self.generateRange(start,end))
                start = nums[i]
                end = nums[i]
        res.append(self.generateRange(start,end))
        return res
    
    def generateRange(self,start,end):
        if start == end:
            return str(start)
        else:
            return str(start)+'->'+str(end)