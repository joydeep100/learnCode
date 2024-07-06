''' Practice https://pythex.org/ 
Syntax
------
\d digit [0-9]
\w letter, digit or underscore
\s space

\D not digit
\W not a word character
\S not space

Quanitfiers
------------
+ one more more
* zero or more
? zero or once
{3} exactly three times
{3,5} three to five times
{3,} three or more times
'''
import re

print(re.search('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',
      '192.1.1.1 1').group())  # gives 192.1.1.1

''' 
Character class
---------------
[aeiou]
[a-f]{2,}
[a-zA-Z]

Anchors and boundaries
----------------------
^ Starts with
$ ends with
\b boundary char

Capture groups
--------------
() 
example 'bat(ma)?n' is the pattern for 'batman'
or bat(ma){0,1}n

'''

# importance of boundary
print(re.search('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',
      'dsa 192.1.1.199 dasd').group())
# gives 192.1.1.199 which is not good enough, so we can give boudaries which is just space or newline

'''so using .group we can view the ouput '''
res = re.search(r'\b\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\b',
                'dsa 192.1.1.1 dasd')  # imp: adding a r passed this, else there was no match
if res:
    print(res.group())
