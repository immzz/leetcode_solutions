class Solution:
    
    def permutation(self,N,num,result):
        if N == 1:
            result.append(num[:])
        else:
            for i in range(N):
                self.permutation(N-1,num,result)
                if N % 2 == 1:
                    temp = num[0]
                    num[0] = num[N-1]
                    num[N-1] = temp
                else:
                    temp = num[i]
                    num[i] = num[N-1]
                    num[N-1] = temp
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        self.permutation(len(num),num,result)
        return result
        
sol = Solution()
print sol.permute([])