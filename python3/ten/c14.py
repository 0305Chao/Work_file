import re
lanuage = 'PythonC#javaPhpphpC#pytC#hon'

def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'
r = re.sub('C#',convert,lanuage)
print(r)