class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[1]*n
        # calculating the left prefix product
        left_product=1
        for i in range(n):
            result[i]=result[i]*left_product
            left_product=left_product*nums[i]
        right_product=1
        for i in range(n-1,-1,-1):
            result[i]=result[i]*right_product
            right_product=right_product*nums[i]
        return result

"""
Intuition: calculating the right prefix and multiplying it with the existing left_prefix in result array.
Time Complexity: O(n)
Space Complexity: O(1)
"""
