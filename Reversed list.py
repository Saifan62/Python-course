list1=[1,2,3,4,5]

temp= []

while len(list1)>0:
    temp.append(list1.pop(-1))

print("Reversed list is:",temp)