class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        visited = [False] * len(nums)
        current,res = [],[]
        self.do(nums,0,visited,current,res)
        return res
    def do(self,nums,i,visited,current,res):
        #print i,visited
        if i == len(nums):
            res.append(current[:])
            return
        j = 0
        while j < len(nums):
            if not visited[j]:
                visited[j] = True
                current.append(nums[j])
                self.do(nums,i+1,visited,current,res)
                current.pop()
                visited[j] = False
                j += 1
                while j < len(nums) and nums[j-1] == nums[j]:
                    j += 1
            else:
                j += 1
        
sol = Solution()
print sol.permuteUnique([1,1])