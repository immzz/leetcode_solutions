class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) < 1:
            return 0
        ptr = 0
        for i in range(1,len(nums)):
            if not nums[ptr] == nums[i]:
                ptr += 1
                nums[ptr] = nums[i]
        return ptr+1

sol = Solution()
a = [1,1,2]
print sol.removeDuplicates(a)
print a