from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        K = min(k, rows + cols - 1)          # 1. cost can't exceed path length
        NEG = -1                             # scores are >= 0, so -1 = impossible

        prev = [[NEG] * (K + 1) for _ in range(cols)]

        for i in range(rows):
            cur = [[NEG] * (K + 1) for _ in range(cols)]
            row = grid[i]
            for j in range(cols):
                val = row[j]
                add = 1 if val else 0
                out = cur[j]

                # 3. pick the "arriving" list(s) once, outside the cost loop
                if i == 0 and j == 0:
                    if add <= K:
                        out[add] = val
                    continue
                top  = prev[j]     if i > 0 else None
                left = cur[j - 1]  if j > 0 else None

                # 2. only costs that can actually occur at this cell
                limit = min(K - add, i + j)
                for c in range(limit + 1):
                    if top is None:
                        best = left[c]
                    elif left is None:
                        best = top[c]
                    else:
                        t, l = top[c], left[c]
                        best = t if t > l else l
                    if best >= 0:
                        out[c + add] = best + val
            prev = cur

        ans = max(prev[cols - 1])
        return ans if ans >= 0 else -1