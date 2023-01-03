import rich
from collections import deque

grid = [
    ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
    ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
    ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
    ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
    ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
    ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
    ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
    ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]



color_map = {
    "Y" : "yellow",
    "G" : "green",
    "W" : "white",
    "B" : "blue",
    "R" : "red",
    "X" : "black",
    "Z" : "gray"
}

def print_grid():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            col = color_map[grid[r][c]]
            rich.print(f"[bold {col}]+[/bold {col}]", end = " ")

        print()


def flood_fill(mat, src, to_col):
    q = deque()
    q.append(src)
    col = mat[src[0]][src[1]]

    while q:
        r, c = q.popleft()
        mat[r][c] = to_col

        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            nr = r + dr 
            nc = c + dc

            if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]):
                if mat[nr][nc] == col:
                    q.append((nr, nc))


print_grid()
print()
flood_fill(grid, (3, 9), 'Z')
print_grid()
