num_str=input("enter a whole number :")
num=int(num_str)

temp_num= num
digitcount=0

if temp_num ==0:
    digitcount=1
else:
    while temp_num > 0:
        temp_num=temp_num // 10
        digitcount=digitcount+1

print(f"the number {num} has {digitcount} digits")