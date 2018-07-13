import json


json_str = '{"name":"qiyue","age":"18"}'
print(json_str)
a = type(json_str)
print (a)
b = json.loads(json_str)
print(b)
print(type(b))
print(b['age'])
c = '[{"name":"qiyue","age":"18","ture":true,"flag":false,"null":" " },{"name":"qiyue","age":"18"}]'

d = json.loads(c)

print(d)
print(type(d))