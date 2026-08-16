class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = int("".join(map(str,digits)))
        result+=1
        result=[int (digit) for digit in str(result)]
        
        return result
