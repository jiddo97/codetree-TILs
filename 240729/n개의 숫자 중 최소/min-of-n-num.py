import sys

n=int(input())
arr=list(map(int,input().split()))

minval=sys.maxsize
cnt=0
for i in range(n):
    if minval>arr[i]:
        minval=arr[i]
        cnt=1
    elif minval==arr[i]:
        cnt+=1

print(minval, cnt)