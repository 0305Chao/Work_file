def chao_user():
    print("Hello world")
chao_user()


def lian_user(kele):
    print("Hello: " + kele.title() + " !")

lian_user('xixi,hello')

def baby(lian,xixi,foot):
    print("\nI have tow baby" + lian + " and " + xixi + foot)
    print("like is : " + xixi)
baby('莲','草莓','蛋糕')


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

describe_pet('willie')


print("实参，形参")

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

