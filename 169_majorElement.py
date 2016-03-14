class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = self.findCan(nums)
        count = 0
        for num in nums:
            if n == num:
                count+=1
        if count >= len(nums)/2.0:
            return n
        else:
            return -1
        
    def findCan(self,nums):
        n = 1
        can = nums[0]
        for index in range(1,len(nums)):
            if nums[index] == can:
                n+=1
            else:
                n-=1
            if n == 0:
                can = nums[index]
                n = 1
        return can
        
        
                