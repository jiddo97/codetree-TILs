arr = list(map(int,input().split()))
sumval=0
sumval2=0
aver=0
cnt=0
for i in range(1,10,2):
    sumval+=arr[i]
for i in range(2,10,3):
    sumval2+=arr[i]
    cnt+=1
aver=sumval2/cnt
print(f"{sumval} {aver:.1f}")