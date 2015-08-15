class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        start = 0
        current_sum = 0
        min = 999999
        for i in xrange(len(nums)):
            current_sum += nums[i]
            while current_sum >= s:
                if i-start+1 < min:
                    min = i-start+1
                current_sum -= nums[start]
                start += 1
            
        return min if min < 999999 else 0
                