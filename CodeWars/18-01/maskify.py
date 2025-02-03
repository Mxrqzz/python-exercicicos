"""
When you buy something, you're often asked to confirm details like your credit card number, 
phone number, or the answer to a security question. However, to prevent someone from 
seeing sensitive information over your shoulder, we mask it.

Your task is to write a function, `maskify`, that replaces all but the last four characters 
of a string with '#'.
"""

StringToMask = input("Enter a phrase to mask: ").strip().lower()


def maskify(string):

    stringCharacter = []

    if string:

        if len(string) <= 4:
            return string

        for letter in string:
            stringCharacter.append(letter)

        for indice in range(len(stringCharacter) - 4):
            stringCharacter[indice] = "#"

        newString = "".join(stringCharacter)
        return newString

    else:
        print("The input string is empty.")
        return None


stringMasked = maskify(StringToMask)

print(stringMasked)
