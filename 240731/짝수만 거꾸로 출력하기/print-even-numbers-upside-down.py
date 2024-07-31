n=int(input())
arr = list(map(int,input().split()))
backarr=[]
for i in range(n):
    if arr[i] %2 == 0 :
        backarr.append(arr[i])
backarr1=backarr[::-1]
for j in backarr1:
    print(j, end=" ")