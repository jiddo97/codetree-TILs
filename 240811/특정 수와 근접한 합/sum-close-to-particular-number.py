# 입력 처리
n, s = map(int, input().split())
numbers = list(map(int, input().split()))

# 초기 총합
total_sum = sum(numbers)

# 초기 최소 차이 (아무런 두 수를 제거하지 않았을 때의 차이로 초기화)
min_diff = float('inf')  # 무한대로 초기화하여 최소값 찾기

# 모든 두 수의 조합을 탐색
for i in range(n):
    for j in range(i + 1, n):
        # 두 수를 제거한 나머지 합
        current_sum = total_sum - numbers[i] - numbers[j]
        # S와의 차이 계산
        current_diff = abs(current_sum - s)
        # 최소 차이 갱신
        if current_diff < min_diff:
            min_diff = current_diff

# 결과 출력
print(min_diff)