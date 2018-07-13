favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
for chao in favorite_languages.values():
    print("\n\n" + chao.title())

for k, v in favorite_languages.items():
    print(k.title()+ " 's favorite language is " + v.title() + " .")

for k, v in favorite_languages.items():
    print(k.title()+ " 's favorite language is " + v.title() + " .")

for k, v in favorite_languages.items():
    print ("\n key is " + k)
    print ("\n value is " + v)
