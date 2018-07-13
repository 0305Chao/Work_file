#数量词
#{3,6}?  就等于 {3}？
# * 匹配0次或者无限多次
# + 匹配1次或者无限次
# ？ 匹配0次或者1次
import re
a = 'python 1111 java ab adfd  dafdsafdsafds fdsfdf'

r = re.findall('[a-z]{3,6}?', a)
print(r)