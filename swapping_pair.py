text_1 = "Seldom"
text_2 = "Bites"
print("Initial String ", "text_1=", text_1, "and text_2=", text_2)

text_1, text_2 = text_2, text_1
print("\nAfter Swapped String ", "text_1=", text_1, "and text_2=", text_2)

print("..........Let's See Practical Implementation of Py-Swapping:.....")
size = int(input("Enter How many numbers do you want to sorting:"))
number_storage = []
for i in range(0, size):
    numbers = int(input("Enter some numbers:"))
    number_storage.append(numbers)

for j in range(0, len(number_storage)):
    for k in range(j+1, len(number_storage)):
        if number_storage[j] > number_storage[k]:
            number_storage[j], number_storage[k] = number_storage[k], number_storage[j]

print("After Swap Technique The Sorted Numbers are:", number_storage)

