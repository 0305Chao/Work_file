def print_student_file(name,gender='女',age=18,college='怀特'):
    print('我叫' + name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')
print_student_file('超','男','23','万腾')

def student_files(names, genders='男', ages=23, colleges='石家庄'):    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_student_file('莲')
print_student_file('嘻嘻','男',23)
a = student_files('有')
print (a)

