grid = [list(map(int, input().split())) for _ in range(4)]

sum_colored = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]

print(sum_colored)