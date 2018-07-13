#数量词
import re
a = 'python 1111 pythonn0pythonnnn java ab adfd  dafdsafdsafds fdsfdf'

r = re.findall('pyton?', a)
print(r)