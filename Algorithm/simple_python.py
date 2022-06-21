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
# The input will be a list of unsorted numbers. 
# we want to get the biggest increase between the number before and after
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

import random
randomlist = []
for i in range(0,20):
    n = random.randint(1,30)
    randomlist.append(n)
print(randomlist)       

# leetcode 1 two sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

# Approach 2: Two-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 

# Approach 3: One-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

# leetcode 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = left + (right-left)//2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot-1
            else:
                left = pivot+1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        # if left == right:
        #     return 0

        while True:
            cur = (left + right) // 2
            v = nums[cur]
            if v == target:
                return cur
            elif left == cur:
                return -1
            elif v < target:
                left = cur
            elif v > target:
                right = cur


# 278. First Bad Version
# You are a product manager and currently leading a team to develop a new product. Unfortunately, 
# the latest version of your product fails the quality check. Since each version is developed based 
# on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. 
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1 , n
        
        if isBadVersion(1):
            return 1
        
        while left < right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid +1
        
        return left

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1 , n
        
        if isBadVersion(1):
            return 1
        
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
            if left == right -1:
                return right


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1

        left = 1
        right = n
        while left <= right:
            pivot = (left + right) // 2
            if isBadVersion(pivot) == True and isBadVersion(pivot - 1) == False:
                return pivot
            elif isBadVersion(pivot) == True:
                right = pivot - 1
            else:
                left = pivot + 1

class Solution:
        def firstBadVersion(self, n: int) -> int:
        l=1
        h=n
        while(l<=h):
            m=(l+h)//2
            if(isBadVersion(m)):
                h=m-1
            else:
                l=m+1
        return l

# leetcode 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] *n
        left, right = 0, n-1
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right = right -1
            else:
                square = nums[left]
                left = left +1
            result[i] = square*square
        return result

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

          return sorted(x*x for x in nums)

# 189. Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Approach 1: Brute Force
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]

# Approach 2: Using Extra Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a

# replace with extra array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
#         # speed up the rotation
        k %= len(nums)
       
        a = nums[-k:]
        b = nums[:len(nums)-k]
        nums[:k] = a 
        nums[k:] = b