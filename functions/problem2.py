#sum of two numbers
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
def sum(num1, num2):
    return num1 + num2

result = sum(num1, num2)
print("Sum of ", num1, "and " ,num2,"=",result)