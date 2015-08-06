class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        temp = 1
        for i in xrange(len(nums)):
            result[i] = temp
            temp *= nums[i]
        temp = 1
        for i in xrange(len(nums)-1,-1,-1):
            result[i] *= temp
            temp *= nums[i]
        return result