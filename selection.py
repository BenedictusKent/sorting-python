from randomlist import randomize
import sys

array = []
randomize(array)

print("Unordered array")
print(array)

num = sys.maxsize                       # Initialize min value
location = -1                           # Initialize location value

for i in range(len(array)):
    for j in range(i, len(array)):
        if num > array[j]:              # Select the lowest value in unsorted array
            num = array[j]
            location = j
    temp = array[i]                     # Swapping
    array[i] = num
    array[location] = temp              # Swap complete
    num = sys.maxsize

print("Ascending array")                # To make descending: sys.maxsize change to -1 and '>' to '<'
print(array)