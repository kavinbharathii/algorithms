
from collections import deque 
import rich

board = [[0 for _ in range(8)] for _ in range(8)]

src = (7, 0)
dest = (0, 7)

q = deque()
visited = set()

q.append((src, 0))

def knight_moves(x: int, y: int) -> list:
    possible_moves = [
        (x - 1, y - 2),
        (x - 2, y - 1),
        (x - 2, y + 1),
        (x - 1, y + 2),
        (x + 1, y - 2),
        (x + 2, y - 1),
        (x + 2, y + 1),
        (x + 1, y + 2)
    ]
    moves = []

    for (kr, kc) in possible_moves:
        if 0 <= kr < len(board) and 0 <= kc < len(board[0]):
            moves.append((kr, kc))

    return moves

while q:
    (curr, dist) = q.popleft()
    visited.add(curr)

    if curr == dest:
        print(f"Minimum no. of moves from {src} to {dest} is {dist}")
        break

    possible_moves = knight_moves(*curr)
    for move in possible_moves:
        if move not in visited:
            q.append((move, dist + 1))

