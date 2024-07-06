import requests

# Function to make a GET request and validate the response
def get_request(url):
    response = requests.get(url)
    
    # Validate response status
    if response.status_code == 200:
        print(f"GET request to {url} succeeded.")
        
        # Validate some JSON values
        data = response.json()
        if 'id' in data and data['id'] == 1:
            print("Response contains 'id' with value 1.")
        if 'title' in data:
            print(f"Title: {data['title']}")
    else:
        print(f"GET request to {url} failed with status code {response.status_code}.")

# Function to make a POST request and validate the response
def post_request(url, payload):
    response = requests.post(url, json=payload)
    
    # Validate response status
    if response.status_code == 201:
        print(f"POST request to {url} succeeded.")
        
        # Validate some JSON values
        data = response.json()
        if 'title' in data and data['title'] == payload['title']:
            print("Response contains the correct 'title'.")
        if 'body' in data and data['body'] == payload['body']:
            print("Response contains the correct 'body'.")
    else:
        print(f"POST request to {url} failed with status code {response.status_code}.")

# Define the API endpoints
get_url = 'https://jsonplaceholder.typicode.com/posts/1'
post_url = 'https://jsonplaceholder.typicode.com/posts'

# Payload for the POST request
post_payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Make the GET request
get_request(get_url)

print("\n" + "="*50 + "\n")

# Make the POST request
post_request(post_url, post_payload)
