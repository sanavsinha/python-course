def add (P,Q):
    return(P+Q)

def subtract(P,Q):
    return (P-Q)

def multiply(P,Q):
    return(P*Q)

print("a=add")
print("b=subtract")
print("c=multiply")
print("d=divide")

choice=input("enter your choice:a,b,c,d:")

num1=int(input("enter a number1 :"))
num2=int(input("enter a number2 :"))


if choice=='a':
    print("the answer is")
    print(num1+num2)
elif choice=='b':
    print("the answer is")
    print(num1-num2)
elif choice=='c':
    print("the answer is")
    print(num1*num2)
elif choice=='d':
    print("the answer is")
    print(num1/num2)
else:
    print("invalid choice")