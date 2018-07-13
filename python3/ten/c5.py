#概括字符集
# \d \D [^] []
# \w 即匹配数字又匹配字母
#\s 空格 字符 空白字符
import re 
a = 'a1b2c3d4f5$%^_ g6h7j8k9'

r = re.findall('[^0-9]',a)
w = re.findall('\w',a)
e = re.findall('\w',a)
q = re.findall('A-Za-z0-9',a)
print(r)
print(w)
print(q)
print(e)