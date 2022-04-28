#Guess the number game
import random
mynum = random.randint(0,9)

print("I have a number in my mind. Can you Guess it?")

while True:
    usernum = int(input("Enter your Guess : "))

    if( mynum == usernum ):
        print("Yes you are Right")
        break
    elif ( mynum > usernum ):
        print("My number is greater than the number you entered. Try again",end="\n\n")
    else:
        print("My number is smaller than the number you entered. Try again",end="\n\n")