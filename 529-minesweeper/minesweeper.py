from collections import deque
from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                      (1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def in_bound(row, col):
            return 0 <= row < m and 0 <= col < n

        def count_mines(row, col):
            count = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if in_bound(nr, nc) and board[nr][nc] == 'M':
                    count += 1
            return count

        def bfs(row, col):
            queue.append((row, col))
            while queue:
                row, col = queue.popleft()
                if visited[row][col]:
                    continue
                visited[row][col] = True

                if board[row][col] == 'M':
                    board[row][col] = 'X'
                    return

                mines = count_mines(row, col)
                if mines > 0:
                    board[row][col] = str(mines)
                else:
                    board[row][col] = 'B'
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if in_bound(nr, nc) and not visited[nr][nc] and board[nr][nc] == 'E':
                            queue.append((nr, nc))

        start_r, start_c = click
        queue = deque()
        bfs(start_r, start_c)
        return board
