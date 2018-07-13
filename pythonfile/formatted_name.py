#formatted_anme.py
print("wu","chao")
def get_formatted_name(first_name,last_name):
    """返回值"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name("jimi","hendrix")

print(musician)


def name_user(first_name,last_name):
    full_name = first_name + ' ' + last_name

    return full_name.title()

while True:
    print("Please tell me your name: ")
    print("(enter 'q' at ant time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")

    if l_name =='q':
        break
    user = name_user(f_name,l_name)
    print("\nHello , " + user + " !")
