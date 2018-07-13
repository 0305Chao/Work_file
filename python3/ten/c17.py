# re.search(chao(.*)chao())
# print(r3.group(0)) 匹配第一个
# print(r3.group(1)) 匹配第二个
# print(r3.group(2)) 如果没有匹配中间的
import re

s = 'file is thie is goog,i python use python'

r = re.search('file.*is', s)
r1 = re.search('file(.*)python', s)
r2 = re.findall('file.*is', s)
r3 = re.search('file(.*)python(.*)python', s)
print(r.group())
print(r1.group(1))
print(r3.group(0))
print(r3.group(1))
print(r3.group(2))
print(r3.group(0,1,2))
print(r3.groups())
print(r2)
