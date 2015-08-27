class Solution(object):
    # corner case: [3,2,0] -> 1
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            while nums[i] != i and nums[i] < len(nums):
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp
        i = 0
        while i < len(nums):
            if nums[i] != i:
                break
            i += 1
        return i

sol = Solution()
print sol.missingNumber([3,2,0])