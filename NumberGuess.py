import random

number = random.randint(1,11)
running = True

while running:
    guess = int(input("Guess the number between 0 and 10: "))

    if guess == number:
        print("You got it!")
        running = False
    else:
        print("Nope!")

