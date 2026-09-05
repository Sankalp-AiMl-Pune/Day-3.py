# Advent of Code 2024 - Day 10: Hoof It

def parse_map(data):
    grid = []
    for line in data.strip().splitlines():
        grid.append([int(c) for c in line.strip()])
    return grid

def find_trailheads(grid):
    heads = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                heads.append((r, c))
    return heads

def get_trails(grid, start_r, start_c):
    # BFS/DFS to find all 9s reachable
    rows, cols = len(grid), len(grid[0])
    stack = [(start_r, start_c)]
    visited_paths = set()
    reachable_nines = set()
    distinct_trails = 0

    # For part 1 we need unique end positions, for part 2 distinct paths
    # So we do DFS tracking path

    def dfs(r, c, path):
        nonlocal distinct_trails
        if grid[r][c] == 9:
            reachable_nines.add((r, c))
            distinct_trails += 1
            return

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == grid[r][c] + 1:
                    dfs(nr, nc, path + [(nr, nc)])

    dfs(start_r, start_c, [(start_r, start_c)])
    return len(reachable_nines), distinct_trails

def solve(data):
    grid = parse_map(data)
    heads = find_trailheads(grid)
    part1 = 0
    part2 = 0
    for r, c in heads:
        p1, p2 = get_trails(grid, r, c)
        part1 += p1
        part2 += p2
    return part1, part2

# --- Run ---
with open("input.txt") as f:
    data = f.read()

p1, p2 = solve(data)
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
