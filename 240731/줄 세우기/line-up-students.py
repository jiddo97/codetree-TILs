class student:
    def __init__(self, h,w,i):
        self.h=h
        self.w=w
        self.i=i

n=int(input())
members=[]
for i in range(1,n+1):
    h,w= tuple(map(int,input().split()))
    members.append(student(h,w,i))

members.sort(key=lambda x:(-x.h,-x.w,x.i))
for p in members:
    print(f"{p.h} {p.w} {p.i}")