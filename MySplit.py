# Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:
# it should accept exactly one argument – a string;
# it should return a list of words created from the string, divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# its name should be mysplit()


def mysplit(strng):
    # Return [] if string is empty or contains whitespaces only
    if strng == '' or strng.isspace():
        return [ ]
    # Prepare a list to return
    lst = []
    # Prepare a word to build subsequent words
    word = ''
    # Check if we are currently inside a word (i.e., if the string starts with a word)
    inword = not strng[0].isspace()
    # Iterate through all the characters in the string
    for x in strng:
        # If we are currently inside a string...
        if inword:
            # ... And the current character is not a space...
            if not x.isspace():
                # ... Update the current word
                word = word + x
            else:
                # ... Otherwise, we've reached the end of the word so we need to append it to the list...
                lst.append(word)
                # ... And signal the fact that we are outside the word now
                inword = False
        else:
            # If we are outside the word and we've reached a non-white character...
            if not x.isspace():
                # ... It means that a new word has begun so we need to remember it and...
                inword = True
                # ... Store the first letter of the new word
                word = x
            else:
                pass
    # If we've left the string and there is a non-empty string in the word, we need to update the list
    if inword:
        lst.append(word)
    # Return the list to the invoker
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))