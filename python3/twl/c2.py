#map
list_x = [1,2,3,4,5,6,7,8]
list_y = [1, 4, 9, 16, 25, 36, 49, 64]
def square(x):
    return x * x 

r = map(square, list_x)
print(list(r))

r = map(lambda x: x * x,list_x)
print(list(r))
