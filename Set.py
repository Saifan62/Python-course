s1= {'blue', 'red', 'green'}
print(s1)
s2= {'yellow', 'red', 'pink'}
print(s2)

s3 = s1.union(s2)
print(s3)
s4= s1.intersection(s2)
print(s4)
s5= s1.symmetric_difference(s2)
print(s5)
s6= s1.difference(s2)
print(s6)
s7= s2.difference(s1)
print(s7)