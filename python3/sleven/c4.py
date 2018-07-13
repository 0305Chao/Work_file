
from enum import Enum
class VIP(Enum):
    YELLOW = 1
    GREEN = 1
    RED = 2
    BREAK = 3


class VIP1(Enum):
    YELLOW = 1
    GREEN = 1
    RED = 2
    BREAK = 3
A = VIP.GREEN is VIP.GREEN
print(A)
B = VIP.GREEN == VIP1.YELLOW
print(B)
C = VIP.GREEN is VIP1.YELLOW
print(C)
D = VIP.GREEN is VIP.YELLOW
print(D)

for v in VIP:
    print(v)

for k in VIP.__members__:
    print(k)
for j in VIP.__members__.items():
    print(j)