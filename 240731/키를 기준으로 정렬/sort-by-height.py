class person:
    def __init__(self, name, h, w):
        self.name = name
        self.h=h
        self.w=w

n=int(input())
members=[]
for _ in range(n):
    name,h,w=tuple(input().split())
    members.append(person(name,int(h),int(w)))


members.sort(key=lambda x:x.h)
for p in members:
    print(f"{p.name} {p.h} {p.w}")