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
        if left == right:
            return 0

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