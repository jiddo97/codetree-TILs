arr = list(map(int,input().split()))
sumval=0
for i in range(10):
    if i == 2 or i == 4 or i == 9:
        sumval+=arr[i]
print(sumval)