class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        

    def peek(self):
        """
        :rtype: int
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        r = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return r
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.s1 == []
        