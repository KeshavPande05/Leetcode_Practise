from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        NEG = float('-inf')   # means "this state is impossible"

        # dp[i][j][c] = max score at cell (i, j) having spent cost c
        dp = [[[NEG] * (k + 1) for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                val  = grid[i][j]
                cost = 1 if val > 0 else 0     # non-zero cell costs 1

                for c in range(k + 1):
                    # Step 1: best score with cost c BEFORE entering this cell
                    if i == 0 and j == 0:
                        before = 0 if c == 0 else NEG   # start: nothing spent yet
                    else:
                        from_top  = dp[i - 1][j][c] if i > 0 else NEG
                        from_left = dp[i][j - 1][c] if j > 0 else NEG
                        before = max(from_top, from_left)

                    if before == NEG:
                        continue                # can't get here with cost c

                    # Step 2: enter this cell -> pay its cost, gain its value
                    new_cost = c + cost
                    if new_cost <= k:
                        dp[i][j][new_cost] = max(dp[i][j][new_cost], before + val)

        # Answer: best score at the bottom-right over any cost <= k
        best = max(dp[rows - 1][cols - 1])
        return best if best != NEG else -1