print("...Set operations With Union, Intersection, etc....")
tuple_ = (4, "digits", 1, "Mazharul", 2, "software")
set_2 = {"Bhuiyan", "Mazharul", "Islm"}

set_t = set(tuple_)
print("Type of Converted Set from tuple:", type(set_t), "& the set is: ", set_t)
print("The Set_2 is: ", set_2)

print("The Union of set_t and set_2(|) is: ", set_t | set_2)
print("The Intersect of set_t & set_2 is: ", set_t & set_2)

# opposite of intersection:
print("Special Operations set_t ^ set_2(items which is not present in both set ): ", set_t ^ set_2)