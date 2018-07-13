#字符集
import re
s = 'abc, acc, adc, afc, ahc'

r = re.findall('a[cf]c', s)
q = re.findall('a[^cf]c',s)
w = re.findall('a[c-f]c',s)
print(q)
print(w)
print (r)

