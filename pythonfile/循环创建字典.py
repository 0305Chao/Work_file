loves = []
for love_number in range(10000):
    new_love = {"超":"爱","莲":"汐汐"}
    loves.append(new_love)
    

for love in loves[:5]:
    print(love)
print("\n说 一万 次")

print("Total number of love: " + str(len(loves)))

'''
loves = []
for love_number in range(10000):
    new_love = {"超":"爱","莲":"汐汐"}
    loves.append(new_love)
    

for love in loves[:5]:
    print(love)
print("\n说 一万 次")

print("Total number of love: " + str(len(loves)))
'''

# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
######################################################################


# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:3]:
    if alien["color"]=="green":
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
for alien in aliens[0:5]:
    print(alien)
print("....")



#####################################################################33
foods = {
    '超':['苹果','葡萄'],
    '莲':['草莓','红枣','酸奶'],
    '汐汐':['奶'],
    }

for name,values in foods.items():
    print("\n "+ name.title() + "'s like is : ")
    for value in values:
        print("\t" + value.title())

#####################################################################
users = {
    'a':{
        'first':'超超',
        'last':'汐汐',
        'location':'医院',
        },
    'b':{
        'first':'莲莲',
        'last':'汐汐',
        'location':'超市',
        
        },
    }
for name,user_info in users.items():
    print("\nUsername: " + name)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation : " + location.title())


###########################################################################
users = {
    'a':{
        'first':'超超',
        'last':'汐汐',
        'location':'医院',
        },
    'b':{
        'first':'莲莲',
        'last':'汐汐',
        'location':'超市',
        
        },
    }
for name,user_info in users.items():
    print("\nUsername: " + name)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation : " + location.title())











