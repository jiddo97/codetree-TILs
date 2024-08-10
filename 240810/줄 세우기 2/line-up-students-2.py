n = int(input())
students = []

for i in range(n):
    h, w = map(int, input().split())
    students.append((h, w, i + 1))  # (키, 몸무게, 번호)

# 정렬: 키를 오름차순으로, 키가 같을 때 몸무게를 내림차순으로
students.sort(key=lambda student: (student[0], -student[1]))

# 결과 출력
for student in students:
    print(student[0], student[1], student[2])