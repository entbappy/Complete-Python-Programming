# # var = 2,4,5,'bappy'
# # print(var)
#
# lis = ['Alu', 'pepsi', 'chocolet', 5673, 67.7, (4+8j), False]
# # print(type(lis))
# # print(type(lis[0:3]))
# lis2 = [12,1,3,5,2,45]
# # lis2.sort()
# # lis2.reverse()
# # print(lis2)
# # print(lis2[::2])
# lis2.append('bappy')
# # lis2.pop()
# # lis2.remove(12)
# lis2.insert(2, 'Alex')
# print(lis2)

# >>>>> Tuple is imutable
# List is mutable
# lis3 = [1,2,3,4]
# lis3[0] = 100
# print(lis3)

tup = (12,3,4,5, 'bappy', 'alex',78465784)
tup = list(tup)
tup = tuple(tup)
# tup[0] = 100
print(tup)

