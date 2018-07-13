#组
# [] 是 或关系
# () 是且关系
import re
a = 'PythonpythonPythonpython,Pythonapythonbpyton'
# 4~8
r = re.findall('(P?)',a)
print(r)