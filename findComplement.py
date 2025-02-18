class Solution:
    def findComplement(self, num: int) -> int:
        num = "{0:b}".format(num)
        newNum = ""
        for n in num:
            if n == '1':
                newNum += '0'
            else:
                newNum += '1'
        newNum = (int(newNum, 2))
        return newNum
