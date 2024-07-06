import json

# Data to be written to the JSON file
data = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland",
    "is_student": False,
    "courses": ["Math", "Science"]
}

# Write the data to a JSON file
with open("Files/data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)  # indent=4 for pretty printing

print(data)