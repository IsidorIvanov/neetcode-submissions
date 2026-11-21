class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp =[]
        for i in range(len(prices)):
            num = prices[i]
            for price in prices[i:]:
                temp.append(price - num)
        temp.append(0)
        return max(temp)            
