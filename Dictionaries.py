my_dict= {}

my_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}

my_dict = {'name': 'John', 1:[2,4,3]}

my_dict = {'name': 'John', 'age': 25}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age']= 27
print(my_dict)

my_dict['Address']= 'New York'
print(my_dict)

my_dict.pop('age')
print(my_dict)


my_dict.clear()
print(my_dict)

