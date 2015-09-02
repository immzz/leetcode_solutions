class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        return "Zero" if num == 0 else " ".join([x for x in self.do(num) if x])
    def do(self,num):
        divider = 1
        while num / divider >= 10:
            divider *= 10
        res = []
        if divider >= 1000000000:
            res.extend(self.do(num/1000000000))
            res.append("Billion")
            res.extend(self.do(num%1000000000))
        elif divider >= 1000000:
            res.extend(self.do(num/1000000))
            res.append("Million")
            res.extend(self.do(num%1000000))
        elif divider >= 1000:
            res.extend(self.do(num/1000))
            res.append("Thousand")
            res.extend(self.do(num%1000))
        elif divider >= 100:
            res.extend(self.do(num/100))
            res.append("Hundred")
            res.extend(self.do(num%100))
        elif num >= 20:
            res = [self.overtens(num),self.ones(num%10)]
        elif num >= 10:
            res = [self.tens(num)]
        else:
            res = [self.ones(num)]
        return res
            
    def overtens(self,num):
        if num >= 90:
            return "Ninety"
        elif num >= 80:
            return "Eighty"
        elif num >= 70:
            return "Seventy"
        elif num >= 60:
            return "Sixty"
        elif num >= 50:
            return "Fifty"
        elif num >= 40:
            return "Forty"
        elif num >= 30:
            return "Thirty"
        elif num >= 20:
            return "Twenty"
    def tens(self,num):
        dic = {10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        return dic[num]
    def ones(self,num):
        dic = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:""}
        return dic[num]
            
            
sol = Solution()
print sol.numberToWords(20)