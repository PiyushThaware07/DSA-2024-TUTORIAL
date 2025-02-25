
# ! Multiple Recursion Calls
def fibonacci(num):
    if num <= 1:
        return num
    last = fibonacci(num-1)
    sLast = fibonacci(num-2)
    return last + sLast
print(fibonacci(4))