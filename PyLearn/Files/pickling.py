import pickle

# Data to be pickled
data = {
    'name': 'Alice',
    'age': 30,
    'job': 'Engineer'
}

# Pickling (serializing) the data
with open('Files/data.pkl', 'wb') as file: # we can see that data.pkl is byte stream and non readable
    pickle.dump(data, file)

print("Data has been pickled and saved to 'data.pkl'.")

# Unpickling (deserializing) the data
with open('Files/data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print("Data has been unpickled from 'data.pkl':")
print(loaded_data)
