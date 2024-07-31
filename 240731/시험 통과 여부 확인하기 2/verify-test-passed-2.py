n=int(input())


sumval=0
cnt=0

for i in  range(n):
    arr = list(map(int,input().split()))
    sumval=sum(arr)
    avr=sumval/4
    if avr>=60:
        print('pass')
        cnt+=1
    else:
        print('fail')

print(cnt)