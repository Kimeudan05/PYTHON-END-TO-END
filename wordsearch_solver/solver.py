import numpy as np

# Directions: horizontal, vertical, diagonal
DIRECTIONS = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, 1), (1, 1), (-1, -1), (1, -1)
]

def find_words(grid, words):
    found = []
    for word in words:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                path = search_from(grid, i, j, word)
                if path:
                    found.append((word, path))
    return found

def search_from(grid, i, j, word):
    rows, cols = len(grid), len(grid[0])
    for di, dj in DIRECTIONS:
        path = []
        x, y = i, j
        for k in range(len(word)):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == word[k]:
                path.append((x, y))
                x += di
                y += dj
            else:
                break
        if len(path) == len(word):
            return path
    return None
