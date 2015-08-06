class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        current = nums[0]
        count = 1
        for i in xrange(1,len(nums)):
            if not nums[i] == current:
                count -= 1
            else:
                count += 1
            if count == 0:
                current = nums[i]
                count = 1
        return current