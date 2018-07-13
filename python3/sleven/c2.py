from enum import Enum

class VIP(Enum):
    YELLOW = '1'
    GREEN = '1'
    BLACK = '3'
    RED = '4'

print(VIP.YELLOW.value)
print(VIP.YELLOW.name)
print(type(VIP.YELLOW))
print(VIP['GREEN'])
#枚举类型 枚举的名字 

for v in VIP:
    print(v)