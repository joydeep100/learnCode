''' 
The json.loads() and json.dumps() functions in Python are used to convert between JSON strings and Python objects.
Here are some examples to illustrate how to use them.
'''

import json

# JSON string
json_string = '''
{
    "name": "Alice",
    "age": 30,
    "city": "Wonderland",
    "is_student": false,
    "courses": ["Math", "Science"]
}
'''

# Convert JSON string to Python dictionary
data = json.loads(json_string)

print("Python object (dictionary):")
print(data)
print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(f"City: {data['city']}")
print(f"Is Student: {data['is_student']}")
print(f"Courses: {data['courses']}")

# dumps example

import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland",
    "is_student": False,
    "courses": ["Math", "Science"]
}

# Convert Python dictionary to JSON string
json_string = json.dumps(data, indent=4)

print("JSON string:")
print(json_string)
