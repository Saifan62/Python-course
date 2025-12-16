import array as arr

array_num = arr.array('i', [1, 2, 3, 3, 4, 5])
print("Original array:" + str(array_num))


print("Num of occurrences of 3 in array: " + str(array_num.count(3)))

array_num.reverse()
print("Reversed array:")
print(str(array_num))