grid = [list(map(int, input().split())) for _ in range(4)]

sum_colored = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3] +grid[1][0]+grid[2][0]+grid[3][0]+grid[2][1]+grid[3][1]+grid[3][2]

print(sum_colored)