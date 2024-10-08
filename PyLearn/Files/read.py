
import os

'''
os.remove('<filename>')
os.rename('<filename>')
os.stat('<filename>') # file size in bytes
'''

print("pwd:", os.getcwd()) # always check this out to get pwd details to contruct path

file = open("Files/lorem.txt")
print(file.read(20))  # will read the first 20 chars
print(file.read())  # will read the remaing chars in the file
file.close()

# read(): Reads the entire file content.
# readline(): Reads one line at a time.
# readlines(): Reads all lines and returns them as a list.

# Reading example
with open("Files/lorem.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        print(line)

# Writing example
with open("Files/haiku.txt", "w", encoding='utf-8') as file: # file gets created if it does not exist
    file.write('hi\n')
    file.write('hi\n')
    file.write('hi\n')

# Append a file
with open('Files/haiku.txt', 'a') as file: # a is append mode
    # Append a new line of text
    file.write("\nThis is an appended line.")
