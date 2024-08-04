import math 

fruits = {
    'apple': 120,
    'banana': 50,
    'cherry': 300,
    'date': 150
}

discounted_fruits = {fruit: math.floor(price * 0.9) for fruit, price in fruits.items()}

print(discounted_fruits)