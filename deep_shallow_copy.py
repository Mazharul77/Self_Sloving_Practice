""" Creating New Objects of the original One
 without automatic modifying the original.
 Changing or modifying one, another is
  not effected when using 'copy-module' and
  defining with the
  deepcopy() : copying process occurs recursively;
  and shallowcopy().

  Let's Implement the deepcopy and shallow copy below:
 """
import copy
print("\tHere Deep Copy & Shallow copy are implemented:\n")
# First we should import the copy module:
list_1 = ["1425", 33, 22, 11, 99.5, ["Mazharul", "Bhuiyan"]]
new_list_2_sh_copy = []
new_list_3_dp_copy = []

print("The Original List is list_1 = ", list_1)
# Now to return shallow copy list we should use only: copy()
new_list_2_sh_copy = copy.copy(list_1)

# Now to return deepcopy list we should use only: deepcopy()
new_list_3_dp_copy = copy.deepcopy(list_1)

# Now Performing some operation on original list:
list_1[5][1:1] = ['Islam']
print("The Modified Original List:", list_1)

print("Now Checking The  Shallow Copy of new_list_2_sh_copy = ", new_list_2_sh_copy)
print("Now Deep Copy Checking of new_list_3_dp_copy = ", new_list_3_dp_copy)
