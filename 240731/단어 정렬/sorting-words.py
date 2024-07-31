n=int(input())
arr=[]
for i in range(n):
    a=input()
    arr.append(a)
arr.sort()
for j in range(n):
    print(arr[j])