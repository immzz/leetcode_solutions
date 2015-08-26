class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        for i in xrange(len(self.q)-1):
            self.q.append(self.q.pop(0))
        return self.q.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        for i in xrange(len(self.q)-1):
            self.q.append(self.q.pop(0))
        r = self.q[0]
        self.q.append(self.q.pop(0))
        return r

    def empty(self):
        """
        :rtype: bool
        """
        return self.q == []
        