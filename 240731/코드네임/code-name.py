class student:
    def __init__(self, name, score):
        self.name=name
        self.score=score

students = []
for _ in range(5):
    name, score = tuple(input().split())
    students.append(student(name, int(score)))

minspy=students[0]

for i in range(5):
    if minspy.score > students[i].score:
        minspy=students[i]

print(f"{minspy.name} {minspy.score}")