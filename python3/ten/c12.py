# re.I 忽略大小写
# re.S 匹配出选中字符后面的字符
# sub 替换
import re
lanuage = 'PythonC#\njavaPhpphp#python'
#4~8
r = re.findall('c#.{2}', lanuage, re.I | re.S)

print(r)


