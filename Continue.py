var = 10 
while var > 0 :
    var =  var - 1
    print(var)
    if var == 5 :
        continue
    print('\nCurrent variable value :', var)
print("Good bye!")

#Practice code#
for i in range(21):
            if i % 10 == 0:
                print(i)
                continue
            print('The Value is:', i)