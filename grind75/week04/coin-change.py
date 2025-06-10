class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        combos = [float('inf')] * (amount + 1)
        combos[0] = 0

        for amount in range(amount + 1):
            for coin in coins:
                if amount - coin >= 0:
                    preAmount = amount - coin
                    combos[amount] = min(combos[amount], combos[preAmount] + 1)

        return combos[amount] if combos[amount] != float('inf') else -1

