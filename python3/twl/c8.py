import time
def decotator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decotator
def f1():
    print('this is a function')

# f = decotator(f1)
# f()

f1()
