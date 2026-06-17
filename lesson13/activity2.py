q=1
n=int(input("enter the number of rows"))

for i in range(n):
    for j in range(i+1):
        print(q ,end="")
        q=q+1
    print()
