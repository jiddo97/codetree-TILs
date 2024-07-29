arr=[0]*15

arr[1],arr[2] = tuple(map(int,input().split()))

for i in range(3,11):
    arr[i] = (arr[i-1]+arr[i-2]) %10

for i in range(1,11):
    print(arr[i],end=" ")