def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P / Q

print("select an operation.")
print("a=add")
print("s=subtract")
print("m=multiply")
print("d=divide")

choice=input("enter your choice(a,s,m,d):")

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice =='b':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice=='m':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice=='d':
    print(num1,"/",num2,"=",divide(num1,num2))

else:
    print("invalid input")