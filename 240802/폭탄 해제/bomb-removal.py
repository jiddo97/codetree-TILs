class bomb:
    def __init__(self, code, color, second):
        self.code=code
        self.color=color
        self.second=second

code, color, second = input().split()
second=int(second)
a=bomb(code,color,second)

print(f"code : {a.code}")
print(f"color : {a.color}")
print(f"second : {a.second}")