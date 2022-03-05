''' Basic
 List Compression
  Is Implemented Here:
   Conditionally or Unconditionally '''

lists_inputs = ["7", "@bhuiyan", 99.4, 5, 7, 2, "art"]
print("Basic List Compression:", [items for items in lists_inputs])

print("\n\t...Let's Find Even/Odd Numbers with List Compression Technique:....")
n = int(input("Enter Size of the inputs you want to enter:"))
numbers = []
for num in range(n):
    numbers.append(int(input("Enter Numbers as Input:")))

print("You have Entered The Inputs:", numbers)
print("The Even Numbers of the Inputs:", [even_num for even_num in numbers if even_num % 2 == 0])
print("The Odd Numbers of the Inputs:", [even_num for even_num in numbers if even_num % 2 != 0])
