import random

def randomize(array):
    repeat = 0
    while True:
        n = random.randint(0,30)
        count = 0
        # Check if there is any duplicate
        for number in range(len(array)):        
            if array[number] == n:
                count += 1
        # If no duplicate, then append to list
        if count == 0:
            array.append(n)
            repeat += 1
        if repeat == 10:
            break