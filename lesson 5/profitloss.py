ac= float(input("enter actual cost:"))
sa=float(input("enter selling amount:"))
if sa > ac: 
    print("profit=",sa-ac)
else:
    print("loss =", ac-sa)