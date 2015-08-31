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
        return (C-A)*(D-B)+(G-E)*(H-F)-max(self.do(A, B, C, D, E, F, G, H),self.do(E, F, G, H, A, B, C, D))
        
    def do(self, A, B, C, D, E, F, G, H):
        if self.isInArea(A,B,C,D,E,H):
            return (min(C,G)-E)*(H-max(B,F))
        elif self.isInArea(A,B,C,D,E,F):
            return (min(C,G)-E)*(min(D,H)-F)
        elif self.isInArea(A,B,C,D,G,H):
            return (G-max(A,E))*(H-max(B,F))
        elif self.isInArea(A,B,C,D,G,F):
            return (G-max(A,E))*(min(D,H)-F)
        return 0
    
    def isInArea(self,A,B,C,D,X,Y):
        return (X>=A and X<=C) and (Y >= B and Y <= D)
    
A,B,C,D,E,F,G,H = 0, 0, 0, 0, -1, -1, 1, 1
sol = Solution()
print sol.computeArea(A,B,C,D,E,F,G,H)
