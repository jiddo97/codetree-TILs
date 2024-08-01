class product:
    def __init__(self, name, code):
        self.name=name
        self.code=code

name, code= input().split()
a=product("codetree", "50")
b=product(name,code)
print(f"product {a.code} is {a.name}")
print(f"product {b.code} is {b.name}")