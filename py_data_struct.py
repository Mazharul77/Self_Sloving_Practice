""" Dictionaries and Tuples are implemented in the next programs within individual files """

# Here We'll implement the followings.........
# insert(index, to_be_inserted_value) like shifting, append(value_to__be_appended), extend(val_or_list_to_be_extended)
# delete(del statement), pop(default_last_value or specific_index-value), remove(value_to_be_removed)
# sort(), count(value_to_be_counted)

print("===== Let's Perform Some Data Structure Operations in python: =====\n")
elements = [3, 4, 5, "start1"]
db_2 = [99, "primary", 99, "End", "db_2"]
optional = ["3", "#", "1", "!", "4", "$", "2",  "@", "z"]

initial_elements = tuple(elements)
print("Original Elements:", elements)

elements.insert(0, "Mazharul")
print("Inserted name-Mazharul In the first position using insert():", elements)

elements.append(0)
print("Original Element Changes with append():", elements)

elements.extend(db_2)
print("Original Element Changes with extend():", elements)

elements.extend([optional])
print("Original Element Changes with extend():", elements)

optional.remove('z')
print("optional Changes with remove():", optional)

# del statement to delete something.................
del elements[-1]
print("Original Elements list Changes with del statement:", elements)

print("Original list Changes  by removing with pop() and Returns the pop-value:", elements.pop(7))

# Now Counting specific item/list.....................
print("\n\tHow many times '99' in elements: ", elements.count(99))

# sorting element's value:
optional.sort()
print("The Sorted Form(ASC-order) of optional is: ", optional)

optional.sort(reverse=True)
print("The Sorted Form(Descending-order) of optional is: ", optional)

print("Initial Elements:", list(initial_elements))
