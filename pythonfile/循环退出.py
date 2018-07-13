'''
a_num = input("输入")

count = 0
while count < 100:
    #print('loop: ',count)
    if count == a_num:
        print ('there you got num:',count)
        choice = input( 'y/n')
        if choice == 'n':
            break
        else:
            a_num = input("输入")
    else:
        print (('loop'),count)
    count +=1
else:
    print('loop:',count)
'''
'''
print_num = input('输入')
count = 0
while count < 100:
    if count == print_num:
        
        print ("you got number:",count)
        choice = input('y/n')
        if chice == 'n':
            break
        else:
            print_num = input('输入')
       
    else:
      print('loop:',count)
    count +=1
else:
  print("loop:",count)

'''


print_num = input('to be')
count = 0
while count < 100:
        if count == print_num:
                print ('There is num:'),count
                choice = input('y or n')
                if choice == 'n':
                        break
                else:
                        while print_num <= count:
                                print_num = input('to be')
                                print ('lod')
        else:
                print ('loop:', count)
        count +=1
else:
        print ('loop:',count)
        
