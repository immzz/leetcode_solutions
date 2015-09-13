class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)):
            if i % 2 == 0 and i + 1 < len(nums) and nums[i+1] < nums[i]:
                self.swap(nums,i,i+1)
            elif i % 2 == 1 and i + 1 < len(nums) and nums[i+1] > nums[i]:
                self.swap(nums,i,i+1)
                
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
                