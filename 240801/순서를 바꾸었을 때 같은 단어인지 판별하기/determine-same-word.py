a=list(input())
b=list(input())
a.sort()
b.sort()
a="".join(a)
b="".join(b)

if a==b:
    print("Yes")
else:
    print("No")