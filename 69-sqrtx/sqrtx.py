class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2 :
            return x
        n=x
        while n*n > x:
            n= (n+x//n)//2
        return n
            
        