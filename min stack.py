class MinStack(object):
    # corner case: push(0),push(1),push(0),getMin,pop,getMin
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min_s = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s.append(x)
        if not self.min_s or self.min_s[-1] >= x:
            self.min_s.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.s[-1] == self.getMin():
            self.min_s.pop()
        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_s[-1]

sol = MinStack()
sol.push(0)
sol.push(1)
sol.push(0)
print sol.s,sol.min_s
sol.getMin()
sol.pop()
sol.getMin()