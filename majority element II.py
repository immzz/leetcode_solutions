class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1,num2,count1,count2 = 0,0,0,0
        for num in nums:
            if count1 == 0 or num == num1:
                num1 = num
                count1 += 1
            elif count2 == 0 or num == num2:
                num2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
            #print num1,num2,count1,count2
        res = []
        count1,count2 = 0,0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
        if count1 > len(nums)/3:
            res.append(num1)
        if count2 > len(nums)/3:
            res.append(num2)
        return res

sol = Solution()
print sol.majorityElement([2,2,4])