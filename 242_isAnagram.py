class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
                
        for char in t:
            if char in count:
                count[char] -=1
            else:
                return False
            if count[char] < 0:
                return False
        
        return True
        
        
        
        """
        return sorted(s) == sorted(t)
        """
        