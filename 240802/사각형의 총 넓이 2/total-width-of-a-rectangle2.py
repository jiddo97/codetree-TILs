n=int(input())
offset=100
maxarr=200
arr=[
    [0 for _ in range(maxarr)]
    for _ in range(maxarr)
]


for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1+offset,x2+offset):
        for j in range(y1+offset,y2+offset):
            arr[i][j]=1


cnt=0
for i in range(maxarr):
    for j in range(maxarr):
        if arr[i][j] ==1:
            cnt+=1
print(cnt)