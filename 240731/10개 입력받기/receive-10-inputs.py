arr=list(map(int,input().split()))
cnt=0
sum=0
for elem in arr:
    if elem == 0 :
        print(f"{sum} {sum/cnt:.1f}")
        break
    cnt+=1
    sum+=elem
print(f"{sum} {sum/cnt:.1f}")