#sum only even index

def recursiveSumEven(arr, idx=0):
    if idx > len(arr)-1:
        return 0
    if idx == len(arr)-1:   #to handle odd length array
        return arr[idx]
    return arr[idx] + recursiveSumEven(arr, idx + 2)
    
# Testing the function
print(recursiveSumEven([1, 2, 3, 4, 5, 6])) # Expected output: 9
print(recursiveSumEven([2, 3])) # Expected output: 2
print(recursiveSumEven([])) # Expected output: 0