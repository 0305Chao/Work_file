import re
a = 'A83C72D1D8E67'
r2 = re.findall('\d',a)
print(r2)
r = re.match('\d',a)
#print (r.span())

r1 = re.search('\d',a)

print(r1.group())

