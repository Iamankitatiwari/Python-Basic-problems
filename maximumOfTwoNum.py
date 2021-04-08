def Maximum(a, b):
    if a >= b:
       return a
    else:
        return b
a = input("Enter a number:")
b = input("Enter a number to compare with:")
print("Maximum Number is:", Maximum(a, b))