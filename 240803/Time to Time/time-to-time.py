a,b,c,d=map(int,input().split())
elapsed=0

while True:
    if a==c and b==d:
        break

    elapsed+=1
    b+=1
    if b==60:
        a+=1
        b=0
print(elapsed)