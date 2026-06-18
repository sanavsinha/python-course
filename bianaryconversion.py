decimalnum=float(input("enter a decimal number to be converted to bianary"))

bianary=""  

while decimalnum>0:
    rem=decimalnum % 2
    bianary=str(int(rem))+bianary
    decimalnum= decimalnum // 2

print ("the bianary number is:",bianary)