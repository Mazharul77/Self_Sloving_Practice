# List reverse with operator : too short way

item_storage = []
n = int(input("Enter Size of the inputs:"))
for i in range(n):
    items = input("Enter list items:")
    item_storage.append(items)
print("The Reverse order of the Items:", item_storage[::-1])
