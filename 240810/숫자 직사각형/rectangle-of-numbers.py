# n과 m을 입력받습니다.
n, m = tuple(map(int, input().split()))

# 2차원 배열을 구현합니다.
arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]
cnt = 1
	
# n * m 크기의 배열에 숫자를 채워 넣습니다.
for i in range(n):
	for j in range(m):
		arr_2d[i][j] = cnt
		cnt += 1
	
# 숫자 직사각형을 출력합니다.
for row in arr_2d:
	for elem in row:
		print(elem, end=" ")
	print()