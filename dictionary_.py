students = {"Name": "Mazharul", "Id": "171-15-1425", "CGPA": 3.97, "Degree": "B.Sc.", "Occupation": "Software-Engineer"}
print("The Defined Dictionary for student:", students)
print("Access Student-Dictionary Keys only using loop:")
for col in students:
    print(col)

print("Access Student-Dictionary Keys only without loop:", students.keys())

print("Access Student-Dictionary Keys and Values:")
for keys in students:
    print(keys, students[keys])

# Students-Dict. key, value with: dict.items() instead of dict.iteritems()
print("\n\tStudents-Dictionary key, values with: items(): ")
for key, value in students.items():
    print(key, ":", value)

# dictionary key, value pairs as tuples with: dict.items() instead of dict.iteritems()
print("\n\tStudents key, value pairs as tuples with: items(): ")
for key_value_pair in students.items():
    print(key_value_pair, ",")