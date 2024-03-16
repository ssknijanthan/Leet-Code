class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set(nums)
        if len(nums)==len(hashset):
            return False
        return True
"""
Inutition: Convert nums list to a set since set doesnt allow duplicate elements
Time Complexity: O(n)
Space Complexity: O(n)
"""
