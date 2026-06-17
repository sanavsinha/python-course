
n = input("Enter the base number: ")
base = int(n)  

exp = input("Enter the exponent (a whole number): ")
exponent = int(exp)

result = 1 
for _ in range(exponent): 
    result = result * base 

print(f"{base} to the power of {exponent} is: {result}")