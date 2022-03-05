
# Python code to reverse a string : # using recursion
# Logic: print(s[1:] + s[0]) until length of string==0

def reverse(str_val, iter_counter):
    if len(str_val) == 0:
        return str_val
    else:
        iter_counter = iter_counter+1
        print("\nPassed String at iteration-", iter_counter, ":", str_val, "& length: ", len(str_val))
        str_val_reversed = reverse(str_val[1:], iter_counter) + str_val[0]
        print("Returned Of the original at Step: ", iter_counter, ":", str_val_reversed)
        return str_val_reversed


str_in = input("Enter String-Text to Reverse:")
counter = 0
print("The original string  is : ", end="")
print(str_in)
print("\n\tThe reversed string(using recursion) is : ", reverse(str_in, counter))
