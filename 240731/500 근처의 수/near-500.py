arr = list(map(int,input().split()))
max500=1
min500=1000
for elem in arr:
    if elem >500 :
        if elem < min500:
            min500 = elem
    else:
        if elem > max500:
            max500=elem

print(max500, min500)