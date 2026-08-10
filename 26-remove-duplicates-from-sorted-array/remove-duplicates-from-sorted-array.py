class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        u=[]
        for i in range(len(nums)):
            if nums[i] in u:
                continue
            else:
                u.append(nums[i])
                nums[k]=nums[i]
                k+=1
        return k
        