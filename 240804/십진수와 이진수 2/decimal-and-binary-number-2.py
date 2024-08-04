n=list(input())
num = 0
for i in range(len(n)):
    num = num * 2 + int(n[i])

newnum = num * 17
digits=[]
while True:
    if newnum < 2:
        digits.append(newnum)
        break

    digits.append(newnum % 2)
    newnum //= 2

# print binary number
for digit in digits[::-1]:
    print(digit, end="")