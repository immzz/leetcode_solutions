class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        lena = len(A)
        if lena == 0: return 0
        mid = lena/2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return self.searchInsert(A[0:mid],target)
        elif A[mid] < target:
            return mid+1+self.searchInsert(A[mid+1:],target)
            
sol = Solution()
print sol.searchInsert([1,3,5,6],4)