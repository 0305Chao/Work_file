import re

a = 'c|c++|c#|python|go|python'
# print(a.index('python') > -1)
# print ('python' in a)
r = re.findall('python', a)
print(r)
if len(r) >0:
    print('字符串中包含python')
else:
    print('No')