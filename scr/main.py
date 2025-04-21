from random import randint 

number = randint(1, 200)
found = False
a = 0
print("\t\tWelcome to GUESS THE NUMBER \n")

while found == False:
    try:
        entry = int(input("\nEnter a number between 1 and 200\nEntry : "))
        while entry < 1 and entry > 200:
            entry = int(input("\nEnter a number between 1 and 200\nEntry : "))
        if entry < number:
            print("The number we're looking for if higher")
        elif entry > number:
            print("The number wer're looking for is lower")
        else:
            found = True
        a += 1
    except:
        print("Please enter a number between 1 and 200\n")

print(f"\nCongratulation you found the right number after {a} {"try" if a == 1 else "tries"} !")