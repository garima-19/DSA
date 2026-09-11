class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        mapping={')':'(',']':'[','}':'{'}
        for i in s:
            if i in ['(','[','{']:
                l.append(i)
            else:
                top=l.pop() if l else '#'
                if mapping[i]!=top:
                    return False

        return not l




            
        