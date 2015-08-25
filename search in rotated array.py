class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.do(nums,target,0,len(nums)-1)
        
    def do(self,nums,target,i,j):
        if not nums or (i > j):
            return -1
        if i == j:
            return i if nums[i] == target else -1
        mid = (i+j)/2
        if nums[i] > nums[j]:
            if nums[mid] > nums[j]:
                if nums[mid] > target:
                    if nums[j] >= target:
                        return self.do(nums,target,mid+1,j)
                    else:
                        return self.do(nums,target,i,mid-1)
                elif nums[mid] < target:
                    return self.do(nums,target,mid+1,j)
                else:
                    return mid
            else:
                if nums[mid] > target:
                    return self.do(nums,target,i,mid-1)
                elif nums[mid] < target:
                    if nums[j] >= target:
                        return self.do(nums,target,mid+1,j)
                    else:
                        return self.do(nums,target,i,mid-1)
                else:
                    return mid
        elif nums[i] < nums[j]:
            if nums[mid] > target:
                return self.do(nums,target,i,mid-1)
            elif nums[mid] < target:
                return self.do(nums,target,mid+1,j)
            else:
                return mid
        else:
            return i if nums[i] == target else -1

sol = Solution()
print sol.search([5,1,3],5)