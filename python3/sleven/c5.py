
from enum import Enum
class VIP(Enum):
    YELLOW = 1
    GREEN = 1
    RED = 2
    BREAK = 3

a = 1
b = 2
c = 3

print(VIP(a))
print(VIP(b))
print(VIP(c))
