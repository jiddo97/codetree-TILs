a,b,c=map(int,input().split())
elapsed=0
d,e,f =11,11,11
while True:
    if d==a and e==b and f==c:
        break
    elif a < d and b <e and c<f:
        elapsed=-1
        break

    elapsed+=1
    f+=1
    if f==60:
        e+=1
        f=0
        if e==24:
            d+=1
            e=0
    
print(elapsed)