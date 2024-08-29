
print([x+1 for x in [1, 2, 3]])  # [2,3,4]

# conditional
print([x+1 for x in range(10) if x % 2 == 0 or x % 2 != 0])  # [3] , since only 2 is even, notice we used x which is on the left most end

# nested
matrix = [[row * col for col in range(3)] for row in range(3)]
print(matrix)
