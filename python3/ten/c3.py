import re


# print(a.index('python') > -1)
# print ('python' in a)
# r = re.findall('python', a)
# print(r)
# if len(r) >0:
#     print('字符串中包含python')
# else:
#     print('No')
a = 'c1c++2c#3python4go5python6'
x = re.findall('\d',a)
r = re.findall('\D',a)
print (x)
print(r)