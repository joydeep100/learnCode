import re

# Define the file path
file_path = 'Regex/sample.txt'

# Create a sample file with some content (for demonstration)
with open(file_path, 'w') as file:
    file.write("""
This is a sample file.
It contains multiple lines.
Here is the first IP address: 192.168.1.1
And here is the second IP address: 10.0.0.1
Another line of text.
End of file.
""")

# Define the regular expression pattern for an IPv4 address
pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Open the file and read its content
with open(file_path, 'r') as file:
    content = file.read()

# Replace all IP addresses with 0.0.0.0
modified_content = re.sub(pattern, '0.0.0.0', content)

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(modified_content)

print("IP addresses have been replaced with 0.0.0.0.")
