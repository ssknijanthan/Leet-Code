class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        profit=0
        while r<len(prices):
               
            if prices[r]>prices[l]:
                profit=max(profit,(prices[r]-prices[l]))
                
            else:
                l=r
            r+=1
        return profit

"""
Intuition: Two pointer approach use l and r pointer  to loop through given prices list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

