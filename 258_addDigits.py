class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num is 0:
            return 0
        elif num%9 is 0:
            return 9
        else:
            return num%9
        