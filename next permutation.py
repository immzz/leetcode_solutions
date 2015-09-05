class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums) - 2
        while l >= 0 and nums[l] >= nums[l+1]:
            l -= 1
        if l == -1:
            nums[:] = nums[::-1]
        else:
            r = len(nums) - 1
            while r > l and nums[r] <= nums[l]:
                r -= 1
            self.swap(nums,l,r)
            h,t = l+1,len(nums)-1
            while h<t:
                self.swap(nums,h,t)
                h += 1
                t -= 1
        
            
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

sol = Solution()
a = [1,2]
sol.nextPermutation(a)
print a