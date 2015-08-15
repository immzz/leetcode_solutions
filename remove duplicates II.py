class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        current = 1
        count = 1
        for i in xrange(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
                if count <= 2:
                    nums[current] = nums[i]
                    current += 1
            else:
                count = 1
                nums[current] = nums[i]
                current += 1
        return current

sol = Solution()
a = [1,1,1,2,2,2,3]
print sol.removeDuplicates(a)
print a