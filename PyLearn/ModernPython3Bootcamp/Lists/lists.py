

list = [1,2,3,4,5]

for number in list:
    print(number)
print('-' * 20)

for i in range(len(list)):
    print(list[i])
print('-' * 20)

for i,j in enumerate(range(len(list))):
    print(list[i], j) # prints the index along with the items
print('-' * 20)

list.append(6) #insert at last
list.insert(0, 99) #insert at start

list.pop() #removes from last
list.pop(0) #remove item at index 0

list.extend([-1,-2,-3])
# print(list)

# list.clear() # will make the entire list empty
print(list)

name = ['joy', 'deep', 'das']
print(name.index('joy'))
# print(name.index('joy2')) #value error

print(name.count('joy')) #1

# These are done in-place
list2 = [1,2,3,4,5]
list2.reverse()
print(list2)

list2.sort()
print(list2)

# Slicing list[start:stop:step]
print([1,2,3,4][1:])
print([1,2,3,4][1:4]) #see the last part should be +1
print([1,2,3,4][::2]) #prints [1,3]
print([1,2,3,4][::-2]) #prints [4,2]

names2 = ['joy', 'deep']
names2[0], names2[1] = names2[1] , names2[0]

print(names2)