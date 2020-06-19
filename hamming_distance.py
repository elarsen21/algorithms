"""
Leetcode 461. Hamming Distance
https://leetcode.com/problems/hamming-distance/

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return(len([x for x in bin(x ^ y) if x == "1"]))