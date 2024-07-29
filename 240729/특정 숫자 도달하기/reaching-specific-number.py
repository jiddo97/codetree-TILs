arr=list(map(int,input().split()))

cnt=0
sum=0

for item in arr:
    if item<250:
        cnt+=1
        sum+=item
    else:
        break

print(f"{sum} {sum/cnt:.1f}")