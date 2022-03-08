def addition(x, y):
    res_add = x + y
    return res_add


def subtraction(x, y):
    res_sub = x - y
    return res_sub


def multiplication(x, y):
    res_mul = x * y
    return res_mul


def division(x, y):
    if y > 0:
        res_div = x / y
    else:
        print("The Dividend can't be 0 .")
    return res_div

