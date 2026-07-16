import random
playing=True
number= str(random.randint(0,9))
print("i will generate a number from 0 to 9")
print("try and guess it")
while playing:
    guess=input("enter your guess")
    if number==guess:
        print("you win")
        print("the number was",number)
    else:
        print(" try again")
        