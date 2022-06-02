# 9. Palindrome Number
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(0, len(x)//2):
            if(x[i] == x[len(x)-1-i]):
                pass
            else:
                return False
            
        return True   