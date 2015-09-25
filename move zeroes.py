class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z_count = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                if i > z_count:
                    nums[z_count] = nums[i]
                    nums[i] = 0
                z_count += 1
        
            