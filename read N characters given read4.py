# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        temp = [''] * 4
        ptr = 0
        while (n > 0):
            readin = read4(temp)
            for i in xrange(min(n,readin)):
                buf[ptr] = temp[i]
                ptr += 1
            if readin < 4:
                break
            n -= min(n,readin)
        return ptr