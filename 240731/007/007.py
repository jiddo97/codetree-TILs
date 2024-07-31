code, loc, time = tuple(input().split())

class cryp:
    def __init__(self, code, loc, time):
        self.code=code
        self.loc=loc
        self.time=time

a=cryp(code,loc,time)

print(f"secret code : {a.code}" )
print(f"meeting point : {a.loc}" )
print(f"time : {a.time}" )