# split() method in python is used to convert string to list and then when required
# we Can use "".join method to join the list according to user requirements
import copy
print("\t...Let's Implement the split() and "".join method step by step:")
str_in = input("Enter Any String To convert ti list:")
li_2 = ["Hi", "I'm", "Mazharul"]
li_3_dpc = copy.deepcopy(li_2)
converted_str_in = str_in.split(" ")
print("Splitted str_in = ", converted_str_in)
print("Joinning The  converted_str_in with + sign =", "+".join(converted_str_in))
print("Joinning The  li_2 with ',' = ", ",".join(li_2))
print("Joinning The  li_3_dpc normally =", "".join(li_2))
