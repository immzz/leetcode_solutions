class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        for i in xrange(len(nums)):
             while (nums[i] != i+1) and (nums[i] > 0) and (nums[i] <= len(nums)) and (nums[nums[i]-1] != nums[i]):
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                return i+1
            i += 1
        return i+1
        
sol = Solution()

print sol.firstMissingPositive([3,4,-1,1])
