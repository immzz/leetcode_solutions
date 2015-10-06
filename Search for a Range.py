class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.searchDo(nums,target,0,len(nums)-1)
        
    def searchDo(self,nums,target,l,r):
        if l > r:
            return [-1,-1]
        if l == r:
            if nums[l] == target:
                return [l,l]
            else:
                return [-1,-1]
        mid = (l+r)/2
        if nums[mid] < target:
            return self.searchDo(nums,target,mid+1,r)
        elif nums[mid] > target:
            return self.searchDo(nums,target,l,mid-1)
        else:
            if nums[l] == target and nums[r] == target:
                return [l,r]
            elif nums[l] == target:
                return [l,self.searchDo(nums,target,mid,r-1)[1]]
            elif nums[r] == target:
                return [self.searchDo(nums,target,l+1,mid)[0],r]
            else:
                return [self.searchDo(nums,target,l+1,mid)[0],self.searchDo(nums,target,mid,r-1)[1]]
        