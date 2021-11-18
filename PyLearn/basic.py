'''
Immutable
- String, Tuple

Mutable
- Dict, Lists, set 
For Set - since we can add elements using the add() method.

ps-Multi line comment'''

'''
Module is a single python file, A package is a collection of python modules.
It can be in several sub directories (an empty __inti__.py file is used to identify sub modules)'''

t=(1,2,3)
print(isinstance(t,tuple))
print(type(t))
print(id(t))
print(hex(id(t)))	#memory address in hex

# max(t)
# min(t)
# pow(x,y)
# sorted(iterable)
# reversed(iterable)
# sum(iterable)
# range(start,stop,step)

#//Converting a list back to string.
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)


#//Replace
'Hello world'.replace('l','z')
#O/P 'Hezzo worzd'

#Sorted <object>.sort() changes the original string, but sorted is like an filter that is applied over
scores_list = [1,2,3,4]
min = sorted(list(set([i for i in scores_list])))[1]

# Justify  - center, ljust & rjust
# print('hello'.center(10,'-'))
# '--hello---'
# print('hello'.rjust(10,'-'))
# '--hello'

#//Working with reverse slicing, A better approach
print([1,2,3,4,5][1:3])
#O/P [2, 3]
print([1,2,3,4,5][1:3][::-1])
#O/P [3, 2]

#precision handling
print('%.5f'%(2/3))
# 0.66667

#absolute diff
abs(2-10)
# 8 

#reversing a range
[i for i in range(3)[::-1]] # or [i for i in range(2,-1,-1)]
# 2 1 0

# Iterating sets - Dont use index to iterate over a set
s=set([1,2,3,3])
for item in s:
	print(item)

#lambda functions - small anonymous function, can take n args. 
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
# o/p 13

#note : if you are working with %, its best to start loop with index 1