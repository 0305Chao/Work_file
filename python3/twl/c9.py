import time
def decotator(func):
    def wrapper(func_name):
        print(time.time())
        func(func_name)
    return wrapper

def decotator2(func):
    def wrapper(*chao):
        print(time.time())
        func(*chao)
    return wrapper

def decotator3(func):
    def wrapper(**chao):
        print(time.time())
        func(**chao)
    return wrapper

@decotator
def f1(func_name):
    print('this is a function' +  func_name)

@decotator2
def f2(func_name1, func_name2,func_name3):
    print('this is a function named ' + func_name1)
    print('this is a function anmed ' + func_name2)
    print('this is a function ' + func_name3)
@decotator3
def f3(**chao):
    print(chao)

f1('xixi love lian love chao')
f2('chao','lian','xixi')
f3(a=1,b=2,c= '123')

