n=int(input())
arr=list(map(int,input().split()))

premaxval=n
while True:
    maxval=0
    
    for i in range(1,premaxval):
        if arr[i] > arr[maxval]:
            maxval=i

    print(maxval+1,end=" ")

    if maxval==0:
        break
    premaxval=maxval