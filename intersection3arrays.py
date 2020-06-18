"""
Leetcode 1213. Intersection of Three Sorted Arrays
https://leetcode.com/problems/intersection-of-three-sorted-arrays/

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
"""

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        h = {}
        for num in arr1 + arr2 + arr3:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        return [num for num, freq in h.items() if freq == 3]
        