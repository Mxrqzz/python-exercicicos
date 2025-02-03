def first_non_repeating_letter(string):
    lowerString = string.lower()
    for i, char in enumerate(lowerString):
        if lowerString.count(char) == 1:
            return string[i]
    return ""