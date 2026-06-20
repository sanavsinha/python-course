rows_str=input("how many rows in your triangle ?")
rows=int(rows_str)

for i in range(1,rows + 1):
    for space_count in range(rows-i):
        print(" ",end="")
    for star_count in range(i):
        print("*",end="")
    print()
