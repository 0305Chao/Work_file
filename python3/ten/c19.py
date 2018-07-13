import json

student = [
            {'name':'chao','age':18,'flag':False},
            {'name':'lian','age':18}
           ]
students = json.dumps(student)
print(type(student))
print(students)
# print(student['name'])
a = '(file is this chao)'
b = json.dumps(a)
print(type(b))
print(b)
