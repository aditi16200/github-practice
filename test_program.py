def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Test 1:", divide(10, 2))
print("Test 2:", divide(10, 0))
