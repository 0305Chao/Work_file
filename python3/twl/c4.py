from functools import reduce
list_x = [1, 4, 9, 16, 25, 36, 49, 64]

r = reduce(lambda x, y: x + y, list_x)
print(r)

list_y = ['1','2','3','4','5','6','7','8']

r = reduce(lambda x,y: x + y, list_y, 'aaa')
print(r)