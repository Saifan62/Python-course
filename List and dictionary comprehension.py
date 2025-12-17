num = [1,2,3,4,5]

even=[x for x in num if x%2==0]
print("List of even numbers using list comprehension:", even)

myDict = {str(x): x**2 for x in [1,2,3,4,5]}
print(myDict)

