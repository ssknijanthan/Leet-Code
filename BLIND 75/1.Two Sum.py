class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps=[]
        for i in range(len(nums)):
            if target-nums[i] in maps:
                return [maps.index(target-nums[i]),i]
            maps.append(nums[i])
"""
Intuition: Check if the target- current element while looping throug nums array is in the maps array whihc basically stores every element after the check

Time Complexity: O(n)
Space COmplexity: O(n)
"""



        
