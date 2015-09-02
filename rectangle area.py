class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x_length = min(C,G)-max(A,E)
        x_length = 0 if x_length < 0 else x_length
        y_length = min(D,H)-max(B,F)
        y_length = 0 if y_length < 0 else y_length
        return (C-A)*(D-B)+(G-E)*(H-F)-(x_length)*(y_length)
        
    
A,B,C,D,E,F,G,H = -2, -2, 2, 2, 3, 3, 4, 4
sol = Solution()
print sol.computeArea(A,B,C,D,E,F,G,H)
