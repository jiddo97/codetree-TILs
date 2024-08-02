class living:
    def __init__(self, name, address, region):
        self.name=name
        self.address=address
        self.region=region

n=int(input())
info = []
for _ in range(n):
    name, address, region = tuple(input().split())
    info.append(living(name, address, region))

target_idx=0
for i , person in enumerate(info):
    if person.name > info[target_idx].name:
        target_idx=i

print(f"name {info[target_idx].name}")
print(f"addr {info[target_idx].address}")
print(f"city {info[target_idx].region}")