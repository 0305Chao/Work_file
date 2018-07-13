import sys
sys.setrecursionlimit(10000)

def add(x, y):
    result = x + y
    return result
def print_code(code):
    print(code)

a = add(1,2)
print(a)
b = print_code ('Python')

print(a,b)