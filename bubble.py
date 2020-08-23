from randomlist import randomize

array = []
randomize(array)

print("Unordered array:")
print(array)

# Bubble sort algorithm
count = 1                                                   # Initialize
while True:                                                 # Iterate endlessly until sorted
    if count > 0:
        count = 0                                           # Reset
        for number in range(len(array)):
            if (number+1) != len(array):
                if array[number] > array[number+1]:         # Change to '<' to make it descending order
                    temp = array[number]
                    array[number] = array[number+1]
                    array[number+1] = temp
                    count += 1
    else:
        break

print("Ascending array:")
print(array)