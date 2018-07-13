prompt = ("\nTell me spmethong and i whill repat it back to you")
prompt += ("\nEnter 'quit' to end the program. ")

#print(prompt)

message = " "
while message != 'quit':
    message = input(prompt)
    
    print(message)
prompt = ("\nTell me spmethong and i whill repat it back to you")
prompt += ("\nEnter 'quit' to end the program. ")

#print(prompt)

message = " "
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I' do love tgo to" + city.title() + " !")
