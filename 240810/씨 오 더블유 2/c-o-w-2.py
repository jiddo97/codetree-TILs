# 입력 받기
n = int(input())
s = input()

# dp 배열 초기화
dp_c = 0  # 'C'가 나타난 횟수
dp_o = 0  # 'C' 다음에 'O'가 나타난 횟수
dp_w = 0  # 'C', 'O' 다음에 'W'가 나타난 횟수

for char in s:
    if char == 'C':
        dp_c += 1
    elif char == 'O':
        dp_o += dp_c
    elif char == 'W':
        dp_w += dp_o

# 결과 출력
print(dp_w)