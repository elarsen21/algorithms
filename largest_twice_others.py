"""
Leetcode 747. Largest Number At Least Twice of Others

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        biggest = float("-inf")
        second = float("-inf")
        biggest_i = 0
        for i in range(len(nums)):
            if nums[i] >= biggest:
                second = biggest
                biggest = nums[i]
                biggest_i = i
            elif nums[i] >= second:
                second = nums[i]
        if biggest >= 2 * second:
            return biggest_i
        return -1