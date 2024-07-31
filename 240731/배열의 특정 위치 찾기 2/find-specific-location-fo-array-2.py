arr=list(map(int,input().split()))
sumval1=0
sumval2=0
for i in range(0,10,2):
    sumval1+=arr[i]
for j in range(1,10,2):
    sumval2+=arr[j]
if sumval1>=sumval2:
    print(sumval1-sumval2)
else:
    print(sumval2-sumval1)