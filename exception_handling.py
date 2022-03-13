print("\n\t ====== Some Exception Handling is Maintained During Programming ======")

try:
    price_ = float(input("Enter The Product Price: "))
    item_quantity = int(input("Enter How many Items Want To Purchase:"))
    total_cost = price_*item_quantity
    # print("Total Cost is:", tc, "and", end=" ")
    no_of_person = int(input("Enter no_of_dividend(To Whom to divide) to be distributed:"))
    per_head_cost = total_cost/no_of_person

    if type(price_) == int:
        print("price_1:", price_, ": Integer-Value Type Price")
    elif type(price_) == float:
        print("price_1:", price_, ":Float-Value Type Price")
    else:
        # This will not be printed
        print("String Type But It throws an Exception if it isn't handled")

except ValueError:
    print("Your Input Value Type Should be Number (integer or float as expected)")
except ZeroDivisionError:
    print("Can't be Divided by 0(no_of_person); Hence dividend must be greater or Equal to 1.")
except TypeError:
    print("Valid Data-type should be Inserted for that Specific Operation")
# except NameError:
#     print("Variable Name Should be defined first to use or variable is misspelled!")
else:
    print("Per Head Cost For ", item_quantity, " items is:", per_head_cost)

finally:
    print("\n\t Thank You!!! ")