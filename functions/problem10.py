def factorial(num):
    if num == 1:
        return 1
    else:
        return num* factorial(num-1)
    

print("factorial of 5 = ", factorial(5))

    