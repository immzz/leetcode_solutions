class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dic = {}
        for (counter,n) in enumerate(num):
            
            if target - n in dic:
                return (min(dic[target - n],counter + 1),max(dic[target - n],counter + 1))
            dic[n] = counter + 1
                
sol = Solution();
print sol.twoSum([3,2,4],6)
