class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged = []
        merged.extend(nums1)
        merged.extend(nums2)
        merged.sort()
        length=len(merged)
        mid= len(merged)//2
        if length%2==0:
            median=(merged[mid-1]+merged[mid])/2.0
        else:
            median=merged[mid]
        return median