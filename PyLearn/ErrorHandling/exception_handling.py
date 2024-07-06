# how to raise custom error's

'''
raise ValueError('Invalid Value')
raise NameError('Invalid Name')
raise TypeError('Invalid Name')
'''

try:
    print('try block')
except NameError as err:
    print(err)

try:
    print('try block')
except (NameError, KeyError) as err:
    print(err)
finally:
    print('prints no matter what')