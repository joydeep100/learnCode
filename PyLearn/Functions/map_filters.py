# A map takes in 2 args (function, iterable)
# iterable can be lists, tuples, dicts, sets, strings etc

# since map generates a map object, which is an iterator. we need to convert into a list to view
print(list(map(lambda num: num*2, [1, 2, 3, 4])))

# using 2 iterables, it will take one from each list
print(list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])))

# A filter takes in 2 args (function, iterable), it filters out non matching items
# iterable can be lists, tuples, dicts, sets, strings etc

# since map generates a map object, which is an iterator. we need to convert into a list to view
print(list(filter(lambda num: num % 2 == 0, [1, 2, 3, 4])))  # [2,4]

# filter does not take multiple iterables :P