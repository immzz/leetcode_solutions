# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.read4_ptr = -1
        self.read_ptr = 0
        self.temp = [None]*4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.read_ptr <= self.read4_ptr:
                buf[i] = self.temp[self.read_ptr]
                self.read_ptr += 1
                i += 1
            else:
                self.read4_ptr = read4(self.temp) - 1
                self.read_ptr = 0
                if self.read4_ptr == -1:
                    return i
        return n
            
            
            
            
sol = Solution()
a = [None] * 10
print sol.read(a,2)