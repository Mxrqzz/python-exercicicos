"""
our friend won't stop texting his girlfriend. It's all he does. All day. Seriously. 
The texts are so mushy too! The whole situation just makes you feel ill. 
Being the wonderful friend that you are, you hatch an evil plot. While he's sleeping, 
you take his phone and change the autocorrect options so that every time he types "you" or "u" it gets changed to "your sister."

Write a function called autocorrect that takes a string and replaces all instances of "you" or "u" 
(not case sensitive) with "your sister" (always lower case).

Return the resulting string.

Here's the slightly tricky part: These are text messages, so there are different forms of "you" and "u".

For the purposes of this kata, here's what you need to support:

"youuuuu" with any number of u characters tacked onto the end
"u" at the beginning, middle, or end of a string, but NOT part of a word
"you" but NOT as part of another word like youtube or bayou
"""

import string


def autocorrect(input):
    # Split the input into a list of words
    string_list = input.split()
    t = len(string_list)

    for i in range(t):
        # Remove punctation temporarily for comparison
        word = string_list[i]
        stripped_word = word.strip(string.punctuation)

        # Check if the word is "you", "u", or "you" with extra "u"s
        if (
            stripped_word == "u"
            or stripped_word.startswith("you")
            and all(char == "u" for char in stripped_word[3:])
        ):
            # Replace the word while preserving original punctuation
            string_list[i] = word.replace(stripped_word, "your sister")

    # Join the list of words back into a single string
    resulting_string = " ".join(string_list)
    return resulting_string

print(autocorrect("I Love youuuuuuu!"))
print(autocorrect("Youuuuu"))
