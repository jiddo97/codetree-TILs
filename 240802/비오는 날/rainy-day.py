class data:
    def __init__(self,date,week,weather):
        self.date=date
        self.week=week
        self.weather=weather



n=int(input())
ans = data("9999-99-99","","")
info = []
for _ in range(n):
    date, week ,weather = tuple(input().split())
    f=data(date,week,weather)
    if weather=="Rain":
        if ans.date >=f.date:
            ans=f

print(ans.date,ans.week,ans.weather)