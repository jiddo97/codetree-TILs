arr= list(map(int,input().split()))

maxval=0
for elem in arr:
    if elem >maxval:
        maxval=elem
print(maxval)