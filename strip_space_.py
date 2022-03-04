'''
Here We are going to stripping
 the extra spaces
  within the string
'''

print("...This program is designed for Stripping text (Remove Extra Space) for left/right or both stripping...\n")

text_space = input("Enter your string text: ")
print("Your given string is: ", text_space)

print("\t Press 'l or L' to remove Left Extra space of the Text (lstrip).")
print("\t Press 'r or R' to remove Right Extra space of the Text (rstrip).")
print("\t Press enter to remove Left & Right Extra space of the Text (strip).")

strip_input = input()
if strip_input == 'l' or strip_input == 'L':
    left_strip = text_space.lstrip()
    print("The String-text after Left- stripping is: ", left_strip, ".")

elif strip_input == 'r' or strip_input == 'R':
    right_strip = text_space.rstrip()
    print("The String-text after Right-stripping is: ", right_strip, ".")

else:
    text_stripped = text_space.strip()
    print("The String-text after Left & Right stripping is: ", text_stripped, ".")

