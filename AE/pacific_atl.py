from math import radians
from tkinter.tix import ROW
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        PAC, ATL = set(), set()

        def dfs(r, c, visit, pre_height):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < pre_height
            ):
                return

            visit.add(r, c)
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, PAC, heights[0][c])
            dfs(ROWS - 1, c, ATL, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, PAC, heights[r][0])
            dfs(r, COLS - 1, ATL, heights[r][COLS - 1])

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in PAC and (r, c) in ATL:
                    result.append((r, c))
        return result
