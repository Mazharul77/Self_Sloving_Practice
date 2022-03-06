# List reverse with operator : too short way
# But String doesn't have reverse() or reversed() function attribute

# ...Reverse Any Input with operators[::-1] Techniques...
print("\n\t...Reverse Any Input:...")
inp_ = input("Enter Your String/Numbers to Reverse:")
print("Your Given Input Is:", inp_)
print("After Reverse Your Output  inp_ = :", inp_[::-1])

print("\n\t...Reverse Any List Input:...")
item_storage = []
n = int(input("Enter Size of the inputs:"))
for i in range(n):
    items = input("Enter list items:")
    item_storage.append(items)
print("The Reverse order of the Items:", item_storage[::-1])

# ............Or List Reverse with Built in Function..........
# With Returned type & Without Modifying Original Input: reversed(variable)
custom_string = input("\n\tEnter String/Number input as List to Reverse With Built-in Function:")
print("After Reverse Your Output,custom_string = ", list(reversed(custom_string)))
print("Original input's Immutable(doesn't modify) with reversed() : custom_string = ", custom_string)

# Without Returned type & Modifying Original Input: variable.reverse()
num = [4, 3, 5, 2]
print("\nOur Another original list: a = ", num)
print("Returned Object of reverse(): ", num.reverse())
print("reverse() Modifies original list: a = ", num)
