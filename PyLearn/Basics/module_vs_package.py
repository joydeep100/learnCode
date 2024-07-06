'''
A module is a single file containing Python code. It can define functions, classes, and variables, 
and it can also include runnable code. Modules help in organizing code logically and making it reusable 
across different parts of an application.

import mymodule

print(mymodule.add(3, 5))       # Output: 8
'''

'''
A package is a way of organizing related modules into a single directory hierarchy. 
A package must contain a special file named __init__.py, which can be empty or can contain 
initialization code for the package. Packages allow you to structure your Python code into namespaces, 
making it easier to manage and maintain.

mypackage/
    __init__.py
    module1.py
    module2.py

from mypackage import module1, module2

'''
