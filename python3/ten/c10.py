#边界匹配
# ^\d 匹配 第一个
# \d{}$ 匹配最后一个
import re
qq = '100000001, 100, 1122, 110, 119'
#4~8
r = re.findall('^\d{3,9}', qq)
print (r)
