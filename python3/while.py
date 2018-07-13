# while for
#CONDITION = True
COUNTER = 1
while COUNTER <=10:
    COUNTER += 1
    print(COUNTER)

a = [['apple', 'orange', 'banana','grape'], (1,2,3)]

for x in a:
    #print (x)
    for y in x:
        # 输出end='' 默认有换行符
        print(y,end='')

for x in range(0,10):
    print(x)
for x in range(0,10,2):
    print(x,end=' | ')
print('\n')
for x in range(10,0,-2):
    print(x,end=' | ')
print('\n')
a = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, 10, 2):
    print(a[i], end=' | ')
print('\n')
b= a[0:len(a):2]
print (b)