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

# calculate the maximum return of investment

def calculate_best_return(lis):
    if len(lis) < 2:
        return 0
    else:
        lis_final = [0]
        a, b = 1, 2
        for idx, i in enumerate(lis):
            for j in lis[idx+1:]:
                if j-i > max(lis_final) :
                    a,b = i,j
                lis_final.append(j-i)
        if max(lis_final) > 0:
            return ("The maximum return is {} from number {} and {}.".format(max(lis_final), a, b))
        else:
            return 0

        
