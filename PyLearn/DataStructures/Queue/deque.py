from collections import deque

queue = deque()

queue.append(1) # O(1)
queue.append(2)
queue.popleft() # O(1)

print(queue)

