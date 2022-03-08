# Assume we need a Fibonacci series up to  a specific size
# along with showing a conditional message if fib_value exceeds a certain limit

print("\t...Fibonaci Series With Loop & Py-Swap Facilities along with Customized Condition:...\n")
size = int(input("Enter The Size Of the Fibonacci Series:"))
counter = 0
fib_m = 0
fib_n = 1


print("The Fibonacci Series For Given Series: ", end=" ")
while counter < size:
    print(fib_n, end=" ")
    fib_m, fib_n = fib_n, fib_m + fib_n
    counter += 1
    if fib_n >= 100:
        print("\n\tThe Custom Initial Expectation is Met Before value of : ", fib_n)
        print("And The Counter Is Reached at Level: ", counter)
        break

    # elif counter < 10:
    #     continue
    # print("\nYour Attempt Limit Exceeds... Try Again Later.....")
