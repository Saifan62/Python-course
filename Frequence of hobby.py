hobby = ('cycling', 'reading', 'gardening', 'reading', 'cycling', 'painting', 'reading')

counter = 0
k= 'reading'

for i in hobby:
    if hobby[i]==k:
        counter += 1
    print(counter,"is the frequency of", k)