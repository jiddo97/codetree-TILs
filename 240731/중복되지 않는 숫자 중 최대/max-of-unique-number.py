n=int(input())
arr=list(map(int,input().split()))
newarr=[]
maxval=-1
for i in range(n):
    if arr[i] not in newarr:
        newarr.append(arr[i])
        if arr[i] > maxval:
            maxval=arr[i]
    
    
print(maxval)