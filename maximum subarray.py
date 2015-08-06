class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        current = nums[0]
        max = current
        for i in xrange(1,len(nums)):
            if current < 0:
                current = 0
            current += nums[i]
            if current > max:
                max = current
        return max