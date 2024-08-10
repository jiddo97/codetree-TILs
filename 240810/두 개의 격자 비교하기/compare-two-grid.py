# 입력 받기
n, m = map(int, input().split())

# 첫 번째 격자 입력
grid1 = [list(map(int, input().split())) for _ in range(n)]

# 두 번째 격자 입력
grid2 = [list(map(int, input().split())) for _ in range(n)]

# 새로운 격자 생성
result_grid = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid1[i][j] == grid2[i][j]:
            result_grid[i][j] = 0
        else:
            result_grid[i][j] = 1

# 결과 출력
for row in result_grid:
    print(' '.join(map(str, row)))