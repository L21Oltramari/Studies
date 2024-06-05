# A program which:
# asks the user for some text;
# checks whether the entered text is a palindrome, and prints the result.
# assume that an empty string isn't a palindrome;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check – treat them as non-existent;
# there are more than a few correct solutions – try to find more than one.

text = input("Enter text: ")

# Remove all spaces...
text = text.replace(' ','')

# ... and check if the word is equal to reversed itself
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("It's a palindrome")
else:
	print("It's not a palindrome")
	
