class Solution(object):
    # corner case: [10,1,2,7,6,1,5],8 -> avoid searching duplicates
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        current = []
        res = []
        self.do(0,candidates,0,current,res,target)
        return res
    def do(self,i,nums,s,current,res,target):
        if s == target:
            res.append(current[:])
            return
        elif s > target:
            return
        else:
            j = i
            while j < len(nums):
                current.append(nums[j])
                self.do(j+1,nums,s+nums[j],current,res,target)
                current.pop()
                j += 1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
            
sol = Solution()
print sol.combinationSum([10,1,2,7,6,1,5],8)