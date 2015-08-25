class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dic = {}
        self.sums = {}
        

    def add(self, number):
        """
        :rtype: nothing
        """
        self.dic[number] = self.dic.get(number,0) + 1
        
        

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        for key in self.dic:
            r = value - key
            if r in self.dic and (r != key or self.dic[r] >= 2):
                return True
        return False
        