class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for char in s:
            num = ord(char)-ord('A')+1
            result = result*26+num
        return result