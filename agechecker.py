try:

    agestr=input("please enter your age:")

    age=int(agestr)

    if age % 2 == 0:
        print(f"your age,{age},is an even number")
    else:
        print(f"your age,{age}, is an odd number")
except ValueError:
    print("oops!thats not a valid age")
    print("enter a integer for your age and try again")

print("program complete")

        