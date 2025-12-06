test_dict = {'Codingal' : 2, 'is' : 1, 'great' : 3}

K=2

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("The number of keys having value", K, "is:" + str(res))
    