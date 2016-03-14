class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # First Solution
        # numSet = set()
        # for num in nums:
        #     if num in numSet:
        #         return True
        #     else:
        #         numSet.add(num)
        # return False
        
        # Second Solution
        return len(nums)!=len(set(nums))