list_x = [1, 4, 9, 16, 25, 36, 49, 64]
list_y = [1, 4, 9, 16, 25, 36, 49, 64]

r = map(lambda x, y: x * x + y, list_x, list_y)
print(list(r))

