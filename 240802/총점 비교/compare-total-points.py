class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n=int(input())
members=[]
for _ in range(n):
    n,k,e,m=tuple(input().split())
    members.append(Student(n,int(k),int(e),int(m)))

members.sort(key=lambda x: ( (x.kor+x.eng+x.math)))

for student in members:
    print(student.name, student.kor,student.eng,student.math)