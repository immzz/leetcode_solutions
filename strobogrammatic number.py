class Solution:
    # @param {string} num
    # @return {boolean}
    # 0 1 2 3 4 5 6 7 8 9
    def isStrobogrammatic(self, num):
        arr = num
        lennums = len(arr)
        mid = int((lennums-1)/2)
        for i in xrange(mid+1):
            if not ((arr[i] == '0' and arr[lennums-1-i] == '0')
                or (arr[i] == '1' and  arr[lennums-1-i] == '1')
                or (arr[i] == '6' and arr[lennums-1-i] == '9')
                or (arr[i] == '8' and  arr[lennums-1-i] == '8')
                or (arr[i] == '9' and arr[lennums-1-i] == '6')):
                return False
        return True