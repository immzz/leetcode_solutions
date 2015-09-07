class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        current_res = []
        res = []
        self.combinationDo(0,0,1,current_res,res,k,n)
        return res
    
    def combinationDo(self,count,current_sum,current_num,current_res,res,k,n):
        if count == k - 1:
            for i in xrange(current_num,10):
                if current_sum + i == n:
                    current_res.append(i)
                    res.append(current_res[:])
                    current_res.pop()
                elif current_sum + i > n:
                    break
        else:
            for i in xrange(current_num,10):
                if current_sum + i < n:
                    current_res.append(i)
                    self.combinationDo(count+1,current_sum+i,i+1,current_res,res,k,n)
                    current_res.pop()
                else:
                    break
                