import random
print("Name:Ranjith Kumar.K\nClass:B.E.CSE (AI&ML)\nFrom:Annur(Mooknur)\nCollage:KGISL INSTITUTE OF TECHNOLOGY\nCOIMBATORE")
user=input("Enter your mode of play(user,machine,exit):")
if user=='user':
    print("you need to guess tyhe number choosen by the machine.")
    print("After each guess, the machine will tell wether it is too high or low or correct")
    low=int(input("set the lower range:"))
    high=int(input("set the upper range:"))
    num_of_guess = random.randint(low,high)
    atmp=0
    while True:
        guess=int(input(f"guess a  number between {low} and {high}:"))
        atmp+=1
        if guess < num_of_guess:
            print("Too low!")
            low = guess+1
        elif guess > num_of_guess:
            print("Too high!")
            high=guess-1
        else:
            print(f"Correct")
            break
elif user=='machine':
    print("think a number within the range you set")
    print("The machine will try to guess the number")
    low=int(input("Enter alower range:"))
    high=int(input("Enter a upper range:"))
    atmp=0
    while True:
        guess=(low+high)//2
        print(f"my guess is:{guess}")
        rd=input("enter 'higher','lower', or 'correct':")
        atmp+=1
        if rd=='higher':
            low=guess+1
        elif rd=='lower':
            high=guess-1
        elif rd=='correct':
            print(f"yeah i won")
            break
        else:
            print("invalid input respond with the above options")
else:
    print("Thank you for plying")