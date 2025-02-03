"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
"""


def find_outlier(integers):

    if integers:
        evenNumbers = []
        oddNumbers = []

        for n in integers:
            if n % 2 == 0:
                evenNumbers.append(n)
            elif n % 2 == 1:
                oddNumbers.append(n)

        if len(evenNumbers) == 1:
            return evenNumbers[0]
        elif len(oddNumbers) == 1:
            return oddNumbers[0]

    else:
        return None


