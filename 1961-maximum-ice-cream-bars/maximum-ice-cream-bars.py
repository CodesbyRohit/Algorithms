
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0] * 100001

        for cost in costs:
            freq[cost] += 1

        count = 0

        for price in range(1, 100001):
            if coins < price:
                break

            buy = min(freq[price], coins // price)

            count += buy
            coins -= buy * price

        return count
