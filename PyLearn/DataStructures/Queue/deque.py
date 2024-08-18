from collections import deque

queue = deque()

queue.append(1) # O(1)
queue.append(2)
queue.append(3)
queue.popleft() # O(1)
queue.pop() # O(1)

print(queue)

