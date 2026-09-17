x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b
print ("addition: ", add(x, y))
print("Subtraction: ", subtract(x, y))
print("Subtraction: ", mul(x, y))
print("Subtraction: ", div(x, y))
