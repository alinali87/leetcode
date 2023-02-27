from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost1 = float('inf')
        reinvest = float('inf')
        profit1 = 0
        total_profit = 0
        for p in prices:
            cost1 = min(cost1, p)       # мин цена на текущем шаге
            profit1 = max(profit1, p - cost1)     # прибыль от первой сделки: используем мин цену с пред.шага и текущую цену
                                        # если текущая прибыль больше предыдущей, то обновляем
            reinvest = min(reinvest, p - profit1)  # из текущей цены вычитаем прибыль - получаем сумму,
                                        # которую мы "доплатили" за текущую акцию с учетом прибыли от первой сделки
            total_profit = max(total_profit, p - reinvest)     # итоговый фин результат от двух сделок = текущая цена - "довложения" с пред шага

        return total_profit


sol = Solution()
prices = [3,3,5,0,0,3,1,4]
a = sol.maxProfit(prices)
assert a == 6

