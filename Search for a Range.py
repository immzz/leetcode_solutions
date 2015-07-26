class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        return self.searchRangeDo(nums,target,0,len(nums)-1)
    
    def searchRangeDo(self,nums,target,l,r):
        if l > r:
            return [-1,-1]
        elif l == r:
            return [l,l] if nums[l] == target else [-1,-1]
        else:
            mid = (l+r)/2
            if target < nums[mid]:
                return self.searchRangeDo(nums,target,l,mid-1)
            elif target > nums[mid]:
                return self.searchRangeDo(nums,target,mid+1,r)
            else:
                left_range = self.searchRangeDo(nums,target,l,mid)
                right_range = self.searchRangeDo(nums,target,mid+1,r)
                if right_range == [-1,-1]:
                    return left_range
                else:
                    return [left_range[0],right_range[1]]
        
        