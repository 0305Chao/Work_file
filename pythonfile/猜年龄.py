Name = input("your name is: ")
Job = input("my Job is: ")
Salary = input("my salary is : ")

#判断年龄是不是 29

real_Age = 29

for i in range(10):

    Age = int(input ('Age:'))
    
    if Age > 29:
        print ("Think samller")
    elif (Age) == 29:
        print  (' Good! 10 RMB!')
        break
    else:
        print ("Think bigger!")

    ##自己还有几次机会,注意括号
    print ((" you still got %s shots ") %(9 - i))
print ('''

Personal ifornamtion of %s:
            Name: %s
            Age : %d
            Job : %s
            Salary: %d

______________________________________________


''' % (Name,Name, Age, Job, Salary))



