"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""

numberList = [5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]


def find_if(seq):
    numberCount = {}
    numbersToDelete = []

    if seq:
        for number in range(len(seq)):
            # * Update the count of the current number in the dictionary
            if seq[number] not in numberCount:
                numberCount[seq[number]] = 0
            numberCount[seq[number]] += 1
        for number in numberCount:
            # * Check if a number count is even, if the number count is even, add it to the list of numbersToDelete.
            if numberCount[number] % 2 == 0:
                numbersToDelete.append(number)
        for number in numbersToDelete:
            # * Delete the numbers in numbersToDelete from the dictionary
            if number in numberCount.keys():
                numberCount.pop(number)
        return list(numberCount.keys())[0]
    else:
        return None
