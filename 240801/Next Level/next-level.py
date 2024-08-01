class user:
    def __init__(self,ids,level):
        self.ids=ids
        self.level=level


user1=user("codetree", "10")
user2=user("codetree", "10")
ids,level = tuple(input().split())
user2.ids=ids
user2.level=level

print(f"user {user1.ids} lv {user1.level}")
print(f"user {user2.ids} lv {user2.level}")