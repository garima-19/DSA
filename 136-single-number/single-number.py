class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            num=nums[i]
            if num in nums[i+1:] or num in nums[0:i]:
                continue
            else:
                return num
            
        