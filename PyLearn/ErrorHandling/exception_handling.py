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

#To except any exception
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"An exception occurred: {e}")

try:
    print('try block')
except (NameError, KeyError, ValueError, IndexError, TypeError) as err:
    print(err)
finally:
    print('prints no matter what')
